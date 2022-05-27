# Name: Neil Schneringer
# ID: 004810739
# Date: May 12th, 2022
# Description: This program interprets a language that can add various battle dots into the Assignment 3 battle dot file.

from antlr4 import *
from COMBATLexer import COMBATLexer
from COMBATParser import COMBATParser
from COMBATVisitor import COMBATVisitor
import os

def main():
    lexer = COMBATLexer(FileStream("insert_input.txt"))
    token_stream = CommonTokenStream(lexer)
    parser = COMBATParser(token_stream)
    visitor = COMBATVisitor()
    while True:
        tree = parser.start()
        if tree.expr() == None: #meaning EOF
            break
        print(tree.toStringTree(recog=parser))
        visitor.visit(tree)


if __name__ == '__main__':
    main()