import datetime
import json
import random
import sys
import uuid


SECS_IN_DAY = 24 * 60 * 60
NUM_LINES = 1000

LOGGERS = ['mysqllogger', 'postgreslogger', 'applogger', 'xylogger']
LOGLEVELS = ['CRITICAL', 'INFO', 'WARNING', 'DEBUG', 'VERBOSE']
TAILS = [
    {'m': 'module1', 'fn': 'function1', 'f': 'file1', 'l': 1, 'P': 'page1',
     'query': 'SELECT a, b FROM table1 where a > b;'},
    {'m': 'module1', 'fn': 'function2', 'f': 'file1', 'l': 10, 'P': 'page2',
     'query': 'SELECT b, a FROM table2 where a < b;'},
    {'m': 'module2', 'fn': 'function3', 'f': 'file2', 'l': 50, 'P': 'page3',
     'query': 'SELECT x, y FROM table3 where x >= y;'},
]


def genFile(file):
  """Generates and writes a file with test log lines.

  Generates a file with a random number of lines in the log line format.
  The number of generated lines is in NUM_LINES to several NUM_LINES range.
  Timestamps are generated for the current date and increase
  by several seconds each.
  Other data fields are randomized.

  Args:
    file: str, Output file name.
  """
  date = datetime.date.today()
  dateStamp = date.isoformat()

  random.seed()

  lines = []
  tsec = random.randrange(SECS_IN_DAY / 2)
  for i in xrange(random.randrange(NUM_LINES, NUM_LINES * 3)):
    time = datetime.time(
        tsec / 3600, (tsec / 60) % 60, tsec % 60)

    tsec += random.randrange(10)

    timeStamp = (dateStamp + ' ' + time.isoformat() + ',' +
                 ('%03d' % random.randrange(1000)))

    reqId = str(uuid.uuid4()).upper()
    proc = random.randrange(10000)
    thread = random.randrange(1000000)
    logger = random.choice(LOGGERS)
    loglevel = random.choice(LOGLEVELS)
    userId = random.randrange(1000)
    timeExpense = random.random()
    tail = random.choice(TAILS)
    m1 = ' %s|%s|%s|%s|%s|%s|%s|(%f)' % (
        timeStamp, reqId, proc, thread, logger, loglevel, userId, timeExpense)
    m2 = ' /* m=<%s>_fn=<%s>_f=<%s>_l=<%s> P=<%s> */ %s' % (
        tail['m'], tail['fn'], tail['f'], tail['l'], tail['P'], tail['query'])
    lines.append('sql_event: ' + json.dumps({'message': m1 + m2}) + '\n')

    with open(file, 'w') as fd:
      fd.writelines(lines)


if __name__ == '__main__':
  genFile(sys.argv[1])

