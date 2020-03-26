import lexer

def main():

    #read the current flow source code in test.lang and store it in variable
    content = ""
    
    with open('test.lang','r') as file:
        content = file.read()

    #
    # Lexer
    #

    # We call the lexer class and initialise it with the source code
    lex = lexer.lexer(content)
    # We now call the tokenize method
    tokens = lex.tokenize()

main()