
import sys
import json

from antlr4 import *
from gen import logMessageLexer
from gen import logMessageParser
from gen import SQLiteLexer
from gen import SQLiteParser
from src import resultListener


def processMessages(data):
  """Parses and cleans log lines.

  Args:
     data: str, A buffer with log lines to parse.
  Returns:
    list<dict>, A list of cleaned log messages as dicts.
  """
  input = InputStream(data)
  lexer = logMessageLexer.logMessageLexer(input)
  stream = CommonTokenStream(lexer)
  parser = logMessageParser.logMessageParser(stream)
  tree = parser.messages()

  # print(tree.toStringTree(recog=parser))

  walker = ParseTreeWalker()
  results = []
  walker.walk(resultListener.ResultListener(results), tree)
  return results


def processSql(sql):
  input = InputStream(sql)
  lexer = SQLiteLexer.SQLiteLexer(input)
  stream = CommonTokenStream(lexer)
  parser = SQLiteParser.SQLiteParser(stream)
  tree = parser.parse()

  # print(tree.toStringTree(recog=parser))

  walker = ParseTreeWalker()
  results = []
  walker.walk(resultListener.SQLListener(results), tree)
  return results


LINE_PREFIX = 'sql_event: '
SKIP = len(LINE_PREFIX)

def processFile(file):
  with open(file) as fd:
    messages = []
    for line in fd.readlines():
      if line.startswith(LINE_PREFIX):
        x = json.loads(line[SKIP:])
        if 'message' in x:
          messages.append(x['message'])
    results = processMessages('\n'.join(messages))
    for res in results:
      sqlreslist = processSql(res['query'])
      res.update(sqlreslist[0])
  return results


if __name__ == '__main__':
  results = processFile(sys.argv[1])
  # for res in results:
  #   print res
  print json.dumps(results)
