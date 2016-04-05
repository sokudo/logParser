import getopt
import itertools
import json
import sys

from antlr4 import *
from gen import logMessageLexer
from gen import logMessageParser
from gen import SQLiteLexer
from gen import SQLiteParser
from src import resultListener


def processMessages(data):
  """Parses log lines and cleans up some fields.

  Args:
     data: str, A buffer with log lines to parse.
  Returns:
    list<dict>, A list of parsed log messages as dicts.
  """
  input = InputStream(data)
  lexer = logMessageLexer.logMessageLexer(input)
  stream = CommonTokenStream(lexer)
  parser = logMessageParser.logMessageParser(stream)
  tree = parser.messages()

  walker = ParseTreeWalker()
  results = []
  walker.walk(resultListener.LogMessagesListener(results), tree)
  return results


def processSql(sql):
  """Parses SQL statements and extracts table, columns, SQL command kind.

  We parse SQL but report kind only as SELECT, INSERT, UPDATE, DELETE or OTHER.

  Args:
     data: str, A buffer with SQL statements to parse.
  Returns:
    list<dict>, A list of dicts with table, columns, sqlOp fields.
  """
  input = InputStream(sql)
  lexer = SQLiteLexer.SQLiteLexer(input)
  stream = CommonTokenStream(lexer)
  parser = SQLiteParser.SQLiteParser(stream)
  results = []
  # Standard SQL parser is exceedingly slow.
  tree = parser.parse()
  walker = ParseTreeWalker()
  walker.walk(resultListener.SQLListener(results), tree)
  return results


LINE_PREFIX = 'sql_event: '
SKIP = len(LINE_PREFIX)


def processFile(file, withSql=False):
  """Process a file with log lines.

  Args:
    file: str, File name.
    withSql:
  Returns:
    list<dict>, A list of dicts with parsed fields.
  """
  with open(file) as fd:
    messages = []
    for line in fd.readlines():
      if line.startswith(LINE_PREFIX):
        x = json.loads(line[SKIP:])
        if 'message' in x:
          messages.append(x['message'])
    results = processMessages('\n'.join(messages))
    if withSql:
      sqlresults = processSql('\n'.join(r['query'] for r in results))
      for res, sqlres in itertools.izip(results, sqlresults):
        res.update(sqlres)
  return results


if __name__ == '__main__':
  opts, args = getopt.getopt(sys.argv[1:], '', ['withSql'])
  withSql = '--withSql' in (opt[0] for opt in opts)
  results = processFile(args[0], withSql=withSql)
  # for res in results:
  #   print res
  print json.dumps(results)
