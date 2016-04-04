from gen import logMessageListener


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





