# Generated from COMBAT.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("(\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\6\5\36\n\5\r\5\16\5\37\3\6\6\6#\n\6\r\6\16\6$\3\6\3")
        buf.write("\6\2\2\7\3\3\5\4\7\5\t\6\13\7\3\2\4\5\2\62;C\\c|\5\2\13")
        buf.write("\f\17\17\"\"\2)\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\23\3\2\2\2\7\26")
        buf.write("\3\2\2\2\t\35\3\2\2\2\13\"\3\2\2\2\r\16\7h\2\2\16\17\7")
        buf.write("k\2\2\17\20\7i\2\2\20\21\7j\2\2\21\22\7v\2\2\22\4\3\2")
        buf.write("\2\2\23\24\7x\2\2\24\25\7u\2\2\25\6\3\2\2\2\26\27\7d\2")
        buf.write("\2\27\30\7g\2\2\30\31\7i\2\2\31\32\7k\2\2\32\33\7p\2\2")
        buf.write("\33\b\3\2\2\2\34\36\t\2\2\2\35\34\3\2\2\2\36\37\3\2\2")
        buf.write("\2\37\35\3\2\2\2\37 \3\2\2\2 \n\3\2\2\2!#\t\3\2\2\"!\3")
        buf.write("\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%&\3\2\2\2&\'\b\6")
        buf.write("\2\2\'\f\3\2\2\2\5\2\37$\3\b\2\2")
        return buf.getvalue()


class COMBATLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    PLAYER = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'fight'", "'vs'", "'begin'" ]

    symbolicNames = [ "<INVALID>",
            "PLAYER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "PLAYER", "WS" ]

    grammarFileName = "COMBAT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


