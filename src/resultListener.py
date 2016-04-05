from gen import logMessageListener
from gen import SQLiteListener


class LogMessagesListener(logMessageListener.logMessageListener):
  """A listener for walking a list of parsed log lines.

  Creates a dict with parsed log fields for each log line
  and collects them into a list.
  """
  def __init__(self, resultsOut):
    self.results = resultsOut
    super(LogMessagesListener, self).__init__()

  def enterMessage(self, ctx):
    self.result = {}

  def exitMessage(self, ctx):
    self.results.append(self.result)
    self.result = None

  def exitTimeStamp(self, ctx):
    self.result['timeStamp'] = ctx.TimeStamp().getText()

  def exitReqId(self, ctx):
    self.result['reqId'] = ctx.Uuid().getText()

  def exitProc(self, ctx):
    self.result['proc'] = ctx.getText()

  def exitThread(self, ctx):
    self.result['thread'] = ctx.getText()

  def exitLogger(self, ctx):
    self.result['logger'] = ctx.getText()

  def exitLogLevel(self, ctx):
    self.result['logLevel'] = ctx.getText()

  def exitUserId(self, ctx):
    self.result['userId'] = ctx.getText()

  def exitTimeExpense(self, ctx):
    self.result['timeExpense'] = ctx.FixedPointNumber().getText()

  def exitAssignment(self, ctx):
    # '<value>' into 'value'.
    self.result[ctx.Name().getText()] = ctx.AngledValue().getText()[1:-1]

  def exitQuery(self, ctx):
    # Removes leading '*/ '.
    self.result['query'] = ctx.getText()[3:]


class SQLListener(SQLiteListener.SQLiteListener):
  """SQL listener for walking the parsed SQL tree.

  Creates a dict with table, columns, SQL command kind (sqlOp) and error count
  for each SQL statement and collects them into a list.
  """

  def __init__(self, resultsOut):
    self.results = resultsOut
    super(SQLListener, self).__init__()

  def enterSql_stmt(self, ctx):
    self.result = {}
    self.result['sqlOp'] = 'OTHER'

  def exitSql_stmt(self, ctx):
    if 'columns' in self.result:
      self.result['columns'] = list(self.result['columns'])
    self.results.append(self.result)
    self.result = None

  def exitTable_name(self, ctx):
    self.result['table'] = ctx.getText()

  def exitColumn_name(self, ctx):
    if 'columns' in self.result:
      self.result['columns'].add(ctx.getText())
    else:
      self.result['columns'] = {ctx.getText()}

  def exitSelect_stmt(self, ctx):
    self.result['sqlOp'] = 'SELECT'

  def exitSelect_core(self, ctx):
    self.result['sqlOp'] = 'SELECT'

  def exitInsert_stmt(self, ctx):
    self.result['sqlOp'] = 'INSERT'

  def exitDelete_stmt(self, ctx):
    self.result['sqlOp'] = 'DELETE'

  def exitUpdate_stmt(self, ctx):
    self.result['sqlOp'] = 'UPDATE'

  def exitError(self, ctx):
    self.result['errorCount'] = self.result.get('errorCount', 0) + 1
