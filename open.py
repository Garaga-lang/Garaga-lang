import GaragaLexer
import GaragaParser
import GaragaInterpreter

from sys import *

lexer = GaragaLexer.Program()
parser = GaragaParser.Program()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    GaragaInterpreter.Program(tree, env)
