
import re

class lexer(object):
    
    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
        
        # Where all the tokens created by lexer will be stored
        tokens = []

        # Create a word list of the source code
        source_code=self.source_code.split()
        
        # This will keep track of the word index we are at in the source code
        source_index = 0

        # Loop through each word in source code to generate tokens
        while source_index < len(source_code):
            
            word = source_code[source_index]

            # This will recognise a variable and create a token for it
            if word == "var": 
                tokens.append(["VAR_DECLARATION", word])

            # This will recognise a word and create an identifier token for it
            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                if word[len(word) - 1] == ";":
                    tokens.append(['IDENTIFIER', word[0:len(word) -1]])
                else:
                    tokens.append(['IDENTIFIER', word])
            
            # This will recognise integer and create an INTEGER token for it
            elif re.match('[0-9]', word):
                if word[len(word) - 1] == ";":
                    tokens.append(['INTEGER', word[0:len(word) -1]])
                else:
                    tokens.append(['INTEGER', word])
            
            # This will recognise operators and create an OPERATOR token for it
            elif word in "=/*=-+":
                tokens.append(['OPERATOR', word])
            
            # If a STATEMENT_END (;) is found at the last character in a word add a STATEMENT_END token
            if word[len(word) - 1] == ";":
                    tokens.append(['STATEMENT_END', ';'])

            # Increases word index after checking it
            source_index += 1
        
        print(tokens)

        # Return created tokens
        return tokens

        #CONTOH PERUBAHAN