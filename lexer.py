import re

#RPAL Language Lexer
#define the token types
TOKEN_TYPES = {
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'INTEGER': r'\d+',
    'OPERATOR': r'[+\-*/<>&.@/:=˜|$!#%^_{}\[\]"‘?]+',
    'STRING': r'\'\'\'\'(\\t|\\n|\\\\|\\\'\'\'|[();,\'\n]|[^()\';,\\])*\'\'\'\'',
    'SPACE': r'[ \t\n]+',
    'COMMENT': r'//[^\n]*\n',
    'PUNCTION': r'[();,]'
}

class Lexer:
    def __init__ (self, program):
        self.program = program
        self.tokens = []
    
    def tokenize(self):
        token_regex = '|'.join(f'(?P<{token_type}>{pattern})' for token_type, pattern in TOKEN_TYPES.items())
        for match in re.finditer(token_regex, self.program):
            token_type = match.lastgroup
            value = match.group(token_type)
            if token_type != 'SPACE' and token_type != 'COMMENT':
                self.tokens.append((token_type, value))
                
    def get_tokens(self):
        return self.tokens
    
#Example usage
if __name__ == '__main__':
    with open('test.rpal', 'r') as file:
            program = file.read()
    lexer = Lexer(program)
    lexer.tokenize()
    tokens = lexer.get_tokens()
    for token in tokens:
        print(token)