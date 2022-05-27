# Generated from COMBAT.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .COMBATParser import COMBATParser
else:
    from COMBATParser import COMBATParser

# This class defines a complete generic visitor for a parse tree produced by COMBATParser.
import os
import shutil
dir = "player_library"
dir2 = "players"

class COMBATVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by COMBATParser#start.
    def visitStart(self, ctx:COMBATParser.StartContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by COMBATParser#timedFightExpr.
    def visitTimedFightExpr(self, ctx: COMBATParser.TimedFightExprContext):
        shutil.rmtree("players")
        bot = "/" + str(ctx.player.text)
        os.system("mkdir players")
        shutil.copytree(dir + bot, dir2 + bot)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by COMBATParser#additionalPlayerExpr.
    def visitAdditionalPlayerExpr(self, ctx: COMBATParser.AdditionalPlayerExprContext):
        bot = "/" + str(ctx.player.text)
        shutil.copytree(dir + bot, dir2 + bot)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by COMBATParser#startFightExpr.
    def visitStartFightExpr(self, ctx:COMBATParser.StartFightExprContext):
        os.system("python A3run_me.py")
        return self.visitChildren(ctx)



del COMBATParser