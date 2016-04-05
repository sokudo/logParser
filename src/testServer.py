import json
import unittest

from src import server

class MyTestCase(unittest.TestCase):
  def test_processFile(self):
    """Tests log line parsing."""
    result = server.processFile('00.txt')
    expected = json.loads(open('00results.txt').read())
    self.assertEqual(result, expected)

  def test_processFileWithSql(self):
    """Tests log line and SQL parsing."""
    result = server.processFile('00.txt', withSql=True)
    expected = json.loads(open('00resultssql.txt').read())
    self.assertEqual(result, expected)


if __name__ == '__main__':
  unittest.main()
