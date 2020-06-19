import GaragaLexer
import GaragaParser
import GaragaInterpreter

from sys import *

if __name__ == '__main__':
    lexer = GaragaLexer.Program()
    parser = GaragaParser.Program()
    env = {}
    while True:
        try:
            text = input('GARAGA > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            GaragaInterpreter.Program(tree, env)