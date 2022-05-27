# Generated from COMBAT.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .COMBATParser import COMBATParser
else:
    from COMBATParser import COMBATParser

# This class defines a complete listener for a parse tree produced by COMBATParser.
class COMBATListener(ParseTreeListener):

    # Enter a parse tree produced by COMBATParser#start.
    def enterStart(self, ctx:COMBATParser.StartContext):
        pass

    # Exit a parse tree produced by COMBATParser#start.
    def exitStart(self, ctx:COMBATParser.StartContext):
        pass


    # Enter a parse tree produced by COMBATParser#timedFightExpr.
    def enterTimedFightExpr(self, ctx:COMBATParser.TimedFightExprContext):
        pass

    # Exit a parse tree produced by COMBATParser#timedFightExpr.
    def exitTimedFightExpr(self, ctx:COMBATParser.TimedFightExprContext):
        pass


    # Enter a parse tree produced by COMBATParser#additionalPlayerExpr.
    def enterAdditionalPlayerExpr(self, ctx:COMBATParser.AdditionalPlayerExprContext):
        pass

    # Exit a parse tree produced by COMBATParser#additionalPlayerExpr.
    def exitAdditionalPlayerExpr(self, ctx:COMBATParser.AdditionalPlayerExprContext):
        pass


    # Enter a parse tree produced by COMBATParser#startFightExpr.
    def enterStartFightExpr(self, ctx:COMBATParser.StartFightExprContext):
        pass

    # Exit a parse tree produced by COMBATParser#startFightExpr.
    def exitStartFightExpr(self, ctx:COMBATParser.StartFightExprContext):
        pass



del COMBATParser