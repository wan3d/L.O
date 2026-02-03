# FUNCTION <value, value?>;

def p_program(t):
    '''
    program : sentences'''

def p_sentences(t):
    '''
    sentences : sentences sentence
                | sentence'''

def p_sentence(t):
    '''
    sentence : expression SEMICOLON'''
    
def p_expression_value(t):
    '''
    expression : TRUE
                | FALSE
    '''
    t[0] = t[1]

def p_expresion(t):
    '''
    expression : AND LARROW expression COMMA expression RARROW 
                | OR LARROW expression COMMA expression RARROW 
                | NOT LARROW expression RARROW 
                | XOR LARROW expression COMMA expression RARROW 
                | BUFFER LARROW expression RARROW 
                | NAND LARROW expression COMMA expression RARROW 
                | NOR LARROW expression COMMA expression RARROW 
                | XNOR LARROW expression COMMA expression RARROW 
    '''
    
    if t[5]: a, b = convertBool(t[3], t[5])
    else: a, b = convertBool(t[3])

    if t[1] == 'AND': print(AND(a, b))
    elif t[1] == 'OR': print(OR(a, b))
    elif t[1] == 'NOT': print(NOT(a))
    elif t[1] == 'XOR': print(XOR(a, b))
    elif t[1] == 'BUFFER': print(BUFFER(a))
    elif t[1] == 'NAND': print(NAND(a, b))
    elif t[1] == 'NOR': print(NOR(a, b))
    elif t[1] == 'XNOR': print(XNOR(a, b))

def convertBool(a, b=None):    
    if a == 'TRUE': a = True
    else: a = False

    if b == 'TRUE': b = True
    else: b = False

    return a, b

def p_error(t):
    print("Syntax error in input!")

from operators import *
from lexer import tokens
import ply.yacc as yacc
from main import input

parser = yacc.yacc()
parser.parse(input)
