import ply.lex as lex
from operators import *

# Define reserved words
keyword = {
    'AND': 'AND',
    'OR': 'OR',
    'NOT': 'NOT',
    'XOR': 'XOR',
    'BUFFER': 'BUFFER',
    'NAND': 'NAND',
    'NOR': 'NOR',
    'XNOR': 'XNOR',
    'TRUE': 'TRUE',
    'FALSE': 'FALSE'
}

def t_ID(t):
    # Recognise keywords
    r'[A-Z]+'

    # If token is in keyword dict, it's a keyword
    # Else is an ID                         
    t.type = keyword.get(t.value, 'ID')
    return t

tokens = (
    'LARROW',
    'VALUE',
    'COMMA',
    'SEMICOLON',
    'RARROW',
    'ID'
) + tuple(keyword.values())

t_LARROW = r'\<'
t_RARROW = r'\>'
t_COMMA = r','
t_SEMICOLON = r';'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

lexer = lex.lex()

'''for tok in lexer:
    print(tok)'''

