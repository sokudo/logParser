from gen import logMessageListener
from gen import SQLiteListener


class ResultListener(logMessageListener.logMessageListener):

  def __init__(self, resultsOut):
    self.results = resultsOut
    super(ResultListener, self).__init__()

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

  def __init__(self, resultsOut):
    self.results = resultsOut
    super(SQLListener, self).__init__()

  def enterSql_stmt(self, ctx):
    self.result = {}

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
    self.result['sqlOp'] = 'select'

  def exitSelect_core(self, ctx):
    self.result['sqlOp'] = 'select'

  def exitInsert_stmt(self, ctx):
    self.result['sqlOp'] = 'insert'

  def exitDelete_stmt(self, ctx):
    self.result['sqlOp'] = 'delete'

  def exitUpdate_stmt(self, ctx):
    self.result['sqlOp'] = 'update'

  def exitError(self, ctx):
    self.result['error'] = self.result.get('error', 0) + 1
