# logParser
Log parser.

Depends on ANTL4 and antlr4-python2-runtime.

$ cd src

# To generates parsers:

$ antlr4 -Dlanguage=Python2 -o ../gen logMessage.g4
$ antlr4 -Dlanguage=Python2 -o ../gen SQLite.g4


# To generate a file 00.dat with test data:
$ python genTestData.py 00.dat

# To run parser with the test data file:
$ python server.py 00.dat
