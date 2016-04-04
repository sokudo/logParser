# Generated from logMessage.g4 by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\27h\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4")
        buf.write(u"\16\t\16\3\2\3\2\5\2\37\n\2\7\2!\n\2\f\2\16\2$\13\2\3")
        buf.write(u"\3\7\3\'\n\3\f\3\16\3*\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\7\bI\n\b\f\b\16")
        buf.write(u"\bL\13\b\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\5\13V\n\13")
        buf.write(u"\3\13\3\13\3\13\7\13[\n\13\f\13\16\13^\13\13\3\f\3\f")
        buf.write(u"\3\r\3\r\3\r\3\r\3\16\3\16\3\16\2\2\17\2\4\6\b\n\f\16")
        buf.write(u"\20\22\24\26\30\32\2\5\3\2\17\17\4\2\6\6\24\24\3\2\b")
        buf.write(u"\f`\2\"\3\2\2\2\4(\3\2\2\2\6?\3\2\2\2\bA\3\2\2\2\nC\3")
        buf.write(u"\2\2\2\fE\3\2\2\2\16J\3\2\2\2\20M\3\2\2\2\22O\3\2\2\2")
        buf.write(u"\24S\3\2\2\2\26_\3\2\2\2\30a\3\2\2\2\32e\3\2\2\2\34\36")
        buf.write(u"\5\4\3\2\35\37\7\25\2\2\36\35\3\2\2\2\36\37\3\2\2\2\37")
        buf.write(u"!\3\2\2\2 \34\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2")
        buf.write(u"#\3\3\2\2\2$\"\3\2\2\2%\'\7\24\2\2&%\3\2\2\2\'*\3\2\2")
        buf.write(u"\2(&\3\2\2\2()\3\2\2\2)+\3\2\2\2*(\3\2\2\2+,\5\6\4\2")
        buf.write(u",-\7\17\2\2-.\5\b\5\2./\7\17\2\2/\60\5\n\6\2\60\61\7")
        buf.write(u"\17\2\2\61\62\5\f\7\2\62\63\7\17\2\2\63\64\5\16\b\2\64")
        buf.write(u"\65\7\17\2\2\65\66\5\32\16\2\66\67\7\17\2\2\678\5\20")
        buf.write(u"\t\289\7\17\2\29:\5\22\n\2:;\7\24\2\2;<\5\24\13\2<=\7")
        buf.write(u"\24\2\2=>\5\26\f\2>\5\3\2\2\2?@\7\21\2\2@\7\3\2\2\2A")
        buf.write(u"B\7\23\2\2B\t\3\2\2\2CD\7\20\2\2D\13\3\2\2\2EF\7\20\2")
        buf.write(u"\2F\r\3\2\2\2GI\n\2\2\2HG\3\2\2\2IL\3\2\2\2JH\3\2\2\2")
        buf.write(u"JK\3\2\2\2K\17\3\2\2\2LJ\3\2\2\2MN\7\20\2\2N\21\3\2\2")
        buf.write(u"\2OP\7\3\2\2PQ\7\22\2\2QR\7\4\2\2R\23\3\2\2\2SU\7\5\2")
        buf.write(u"\2TV\7\24\2\2UT\3\2\2\2UV\3\2\2\2VW\3\2\2\2W\\\5\30\r")
        buf.write(u"\2XY\t\3\2\2Y[\5\30\r\2ZX\3\2\2\2[^\3\2\2\2\\Z\3\2\2")
        buf.write(u"\2\\]\3\2\2\2]\25\3\2\2\2^\\\3\2\2\2_`\7\r\2\2`\27\3")
        buf.write(u"\2\2\2ab\7\26\2\2bc\7\7\2\2cd\7\16\2\2d\31\3\2\2\2ef")
        buf.write(u"\t\4\2\2f\33\3\2\2\2\b\36\"(JU\\")
        return buf.getvalue()


class logMessageParser ( Parser ):

    grammarFileName = "logMessage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"'/*'", u"'_'", u"'='", 
                     u"'CRITICAL'", u"'INFO'", u"'WARNING'", u"'DEBUG'", 
                     u"'VERBOSE'", u"<INVALID>", u"<INVALID>", u"'|'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"UncomQuery", 
                      u"AngledValue", u"PS", u"DecimalNumber", u"TimeStamp", 
                      u"FixedPointNumber", u"Uuid", u"WS", u"NL", u"Name", 
                      u"ErrorChar" ]

    RULE_messages = 0
    RULE_message = 1
    RULE_timeStamp = 2
    RULE_reqId = 3
    RULE_proc = 4
    RULE_thread = 5
    RULE_logger = 6
    RULE_userId = 7
    RULE_timeExpense = 8
    RULE_source = 9
    RULE_query = 10
    RULE_assignment = 11
    RULE_logLevel = 12

    ruleNames =  [ u"messages", u"message", u"timeStamp", u"reqId", u"proc", 
                   u"thread", u"logger", u"userId", u"timeExpense", u"source", 
                   u"query", u"assignment", u"logLevel" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    UncomQuery=11
    AngledValue=12
    PS=13
    DecimalNumber=14
    TimeStamp=15
    FixedPointNumber=16
    Uuid=17
    WS=18
    NL=19
    Name=20
    ErrorChar=21

    def __init__(self, input):
        super(logMessageParser, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class MessagesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(logMessageParser.MessagesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def message(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(logMessageParser.MessageContext)
            else:
                return self.getTypedRuleContext(logMessageParser.MessageContext,i)


        def NL(self, i=None):
            if i is None:
                return self.getTokens(logMessageParser.NL)
            else:
                return self.getToken(logMessageParser.NL, i)

        def getRuleIndex(self):
            return logMessageParser.RULE_messages

        def enterRule(self, listener):
            if hasattr(listener, "enterMessages"):
                listener.enterMessages(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMessages"):
                listener.exitMessages(self)




    def messages(self):

        localctx = logMessageParser.MessagesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_messages)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==logMessageParser.TimeStamp or _la==logMessageParser.WS:
                self.state = 26
                self.message()
                self.state = 28
                _la = self._input.LA(1)
                if _la==logMessageParser.NL:
                    self.state = 27
                    self.match(logMessageParser.NL)


                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MessageContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(logMessageParser.MessageContext, self).__init__(parent, invokingState)
            self.parser = parser

        def timeStamp(self):
            return self.getTypedRuleContext(logMessageParser.TimeStampContext,0)


        def PS(self, i=None):
            if i is None:
                return self.getTokens(logMessageParser.PS)
            else:
                return self.getToken(logMessageParser.PS, i)

        def reqId(self):
            return self.getTypedRuleContext(logMessageParser.ReqIdContext,0)


        def proc(self):
            return self.getTypedRuleContext(logMessageParser.ProcContext,0)


        def thread(self):
            return self.getTypedRuleContext(logMessageParser.ThreadContext,0)


        def logger(self):
            return self.getTypedRuleContext(logMessageParser.LoggerContext,0)


        def logLevel(self):
            return self.getTypedRuleContext(logMessageParser.LogLevelContext,0)


        def userId(self):
            return self.getTypedRuleContext(logMessageParser.UserIdContext,0)


        def timeExpense(self):
            return self.getTypedRuleContext(logMessageParser.TimeExpenseContext,0)


        def WS(self, i=None):
            if i is None:
                return self.getTokens(logMessageParser.WS)
            else:
                return self.getToken(logMessageParser.WS, i)

        def source(self):
            return self.getTypedRuleContext(logMessageParser.SourceContext,0)


        def query(self):
            return self.getTypedRuleContext(logMessageParser.QueryContext,0)


        def getRuleIndex(self):
            return logMessageParser.RULE_message

        def enterRule(self, listener):
            if hasattr(listener, "enterMessage"):
                listener.enterMessage(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMessage"):
                listener.exitMessage(self)




    def message(self):

        localctx = logMessageParser.MessageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_message)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==logMessageParser.WS:
                self.state = 35
                self.match(logMessageParser.WS)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.timeStamp()
            self.state = 42
            self.match(logMessageParser.PS)
            self.state = 43
            self.reqId()
            self.state = 44
            self.match(logMessageParser.PS)
            self.state = 45
            self.proc()
            self.state = 46
            self.match(logMessageParser.PS)
            self.state = 47
            self.thread()
            self.state = 48
            self.match(logMessageParser.PS)
            self.state = 49
            self.logger()
            self.state = 50
            self.match(logMessageParser.PS)
            self.state = 51
            self.logLevel()
            self.state = 52
            self.match(logMessageParser.PS)
            self.state = 53
            self.userId()
            self.state = 54
            self.match(logMessageParser.PS)
            self.state = 55
            self.timeExpense()
            self.state = 56
            self.match(logMessageParser.WS)
            self.state = 57
            self.source()
            self.state = 58
            self.match(logMessageParser.WS)
            self.state = 59
            self.query()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TimeStampContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(logMessageParser.TimeStampContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TimeStamp(self):
            return self.getToken(logMessageParser.TimeStamp, 0)

        def getRuleIndex(self):
            return logMessageParser.RULE_timeStamp

        def enterRule(self, listener):
            if hasattr(listener, "enterTimeStamp"):
                listener.enterTimeStamp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTimeStamp"):
                listener.exitTimeStamp(self)




    def timeStamp(self):

        localctx = logMessageParser.TimeStampContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_timeStamp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(logMessageParser.TimeStamp)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReqIdContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(logMessageParser.ReqIdContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Uuid(self):
            return self.getToken(logMessageParser.Uuid, 0)

        def getRuleIndex(self):
            return logMessageParser.RULE_reqId

        def enterRule(self, listener):
            if hasattr(listener, "enterReqId"):
                listener.enterReqId(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitReqId"):
                listener.exitReqId(self)




    def reqId(self):

        localctx = logMessageParser.ReqIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_reqId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(logMessageParser.Uuid)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(logMessageParser.ProcContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DecimalNumber(self):
            return self.getToken(logMessageParser.DecimalNumber, 0)

        def getRuleIndex(self):
            return logMessageParser.RULE_proc

        def enterRule(self, listener):
            if hasattr(listener, "enterProc"):
                listener.enterProc(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitProc"):
                listener.exitProc(self)




    def proc(self):

        localctx = logMessageParser.ProcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_proc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(logMessageParser.DecimalNumber)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ThreadContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(logMessageParser.ThreadContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DecimalNumber(self):
            return self.getToken(logMessageParser.DecimalNumber, 0)

        def getRuleIndex(self):
            return logMessageParser.RULE_thread

        def enterRule(self, listener):
            if hasattr(listener, "enterThread"):
                listener.enterThread(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitThread"):
                listener.exitThread(self)




    def thread(self):

        localctx = logMessageParser.ThreadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_thread)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(logMessageParser.DecimalNumber)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LoggerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(logMessageParser.LoggerContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return logMessageParser.RULE_logger

        def enterRule(self, listener):
            if hasattr(listener, "enterLogger"):
                listener.enterLogger(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLogger"):
                listener.exitLogger(self)




    def logger(self):

        localctx = logMessageParser.LoggerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_logger)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << logMessageParser.T__0) | (1 << logMessageParser.T__1) | (1 << logMessageParser.T__2) | (1 << logMessageParser.T__3) | (1 << logMessageParser.T__4) | (1 << logMessageParser.T__5) | (1 << logMessageParser.T__6) | (1 << logMessageParser.T__7) | (1 << logMessageParser.T__8) | (1 << logMessageParser.T__9) | (1 << logMessageParser.UncomQuery) | (1 << logMessageParser.AngledValue) | (1 << logMessageParser.DecimalNumber) | (1 << logMessageParser.TimeStamp) | (1 << logMessageParser.FixedPointNumber) | (1 << logMessageParser.Uuid) | (1 << logMessageParser.WS) | (1 << logMessageParser.NL) | (1 << logMessageParser.Name) | (1 << logMessageParser.ErrorChar))) != 0):
                self.state = 69
                _la = self._input.LA(1)
                if _la <= 0 or _la==logMessageParser.PS:
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UserIdContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(logMessageParser.UserIdContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DecimalNumber(self):
            return self.getToken(logMessageParser.DecimalNumber, 0)

        def getRuleIndex(self):
            return logMessageParser.RULE_userId

        def enterRule(self, listener):
            if hasattr(listener, "enterUserId"):
                listener.enterUserId(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUserId"):
                listener.exitUserId(self)




    def userId(self):

        localctx = logMessageParser.UserIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_userId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(logMessageParser.DecimalNumber)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TimeExpenseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(logMessageParser.TimeExpenseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FixedPointNumber(self):
            return self.getToken(logMessageParser.FixedPointNumber, 0)

        def getRuleIndex(self):
            return logMessageParser.RULE_timeExpense

        def enterRule(self, listener):
            if hasattr(listener, "enterTimeExpense"):
                listener.enterTimeExpense(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTimeExpense"):
                listener.exitTimeExpense(self)




    def timeExpense(self):

        localctx = logMessageParser.TimeExpenseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_timeExpense)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(logMessageParser.T__0)
            self.state = 78
            self.match(logMessageParser.FixedPointNumber)
            self.state = 79
            self.match(logMessageParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SourceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(logMessageParser.SourceContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(logMessageParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(logMessageParser.AssignmentContext,i)


        def WS(self, i=None):
            if i is None:
                return self.getTokens(logMessageParser.WS)
            else:
                return self.getToken(logMessageParser.WS, i)

        def getRuleIndex(self):
            return logMessageParser.RULE_source

        def enterRule(self, listener):
            if hasattr(listener, "enterSource"):
                listener.enterSource(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSource"):
                listener.exitSource(self)




    def source(self):

        localctx = logMessageParser.SourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_source)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(logMessageParser.T__2)
            self.state = 83
            _la = self._input.LA(1)
            if _la==logMessageParser.WS:
                self.state = 82
                self.match(logMessageParser.WS)


            self.state = 85
            self.assignment()
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 86
                    _la = self._input.LA(1)
                    if not(_la==logMessageParser.T__3 or _la==logMessageParser.WS):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()
                    self.state = 87
                    self.assignment() 
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QueryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(logMessageParser.QueryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def UncomQuery(self):
            return self.getToken(logMessageParser.UncomQuery, 0)

        def getRuleIndex(self):
            return logMessageParser.RULE_query

        def enterRule(self, listener):
            if hasattr(listener, "enterQuery"):
                listener.enterQuery(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitQuery"):
                listener.exitQuery(self)




    def query(self):

        localctx = logMessageParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(logMessageParser.UncomQuery)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(logMessageParser.AssignmentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(logMessageParser.Name, 0)

        def AngledValue(self):
            return self.getToken(logMessageParser.AngledValue, 0)

        def getRuleIndex(self):
            return logMessageParser.RULE_assignment

        def enterRule(self, listener):
            if hasattr(listener, "enterAssignment"):
                listener.enterAssignment(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssignment"):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = logMessageParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(logMessageParser.Name)
            self.state = 96
            self.match(logMessageParser.T__4)
            self.state = 97
            self.match(logMessageParser.AngledValue)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LogLevelContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(logMessageParser.LogLevelContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return logMessageParser.RULE_logLevel

        def enterRule(self, listener):
            if hasattr(listener, "enterLogLevel"):
                listener.enterLogLevel(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLogLevel"):
                listener.exitLogLevel(self)




    def logLevel(self):

        localctx = logMessageParser.LogLevelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_logLevel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << logMessageParser.T__5) | (1 << logMessageParser.T__6) | (1 << logMessageParser.T__7) | (1 << logMessageParser.T__8) | (1 << logMessageParser.T__9))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





