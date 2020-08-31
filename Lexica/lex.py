#------------------------------------------------------------
# lex.py
#
# Analisador lexico
# Brendow Paolillo Castro Isidoro
# ------------------------------------------------------------
import ply.lex as lex

##Definicoes

tokens = (
    'MAIS',
    'MENOS',
    'MULTIPLICACAO',
    'DIVISAO',
    'DOIS_PONTOS',
    'VIRGULA',
    'MENOR',
    'MAIOR',
    'IGUAL',
    'DIFERENTE', 
    'MENOR_IGUAL', 
    'MAIOR_IGUAL', 
    'E_LOGICO',
    'OU_LOGICO',
    'NEGACAO',
    'ABRE_PARENTESE',
    'FECHA_PARENTESE',
    'ABRE_COLCHETE',
    'FECHA_COLCHETE',
    'SE', 
    'ENTAO', 
    'SENAO', 
    'FIM', 
    'REPITA', 
    'ATE', 
    'ATRIBUICAO', 
    'LEIA', 
    'ESCREVA', 
    'RETORNA', 
    'INTEIRO', 
    'FLUTUANTE', 
    'NUM_INTEIRO', 
    'NUM_PONTO_FLUTUANTE', 
    'NUM_NOTACAO_CIENTIFICA', 
    'ID',
    'FUNCAO',
)

##REGRAS SIMPLES
t_MAIS              = r'\+'
t_MENOS             = r'-'
t_MULTIPLICACAO     = r'\*'
t_DIVISAO           = r'\/'
t_DOIS_PONTOS       = r':'
t_VIRGULA           = r','
t_MENOR             = r'<'
t_MAIOR             = r'>'
t_ATRIBUICAO        = r'='
t_MENOR_IGUAL       = r'<='
t_MAIOR_IGUAL       = r'>='
t_IGUAL             = r'=='
t_DIFERENTE         = r'!='
t_E_LOGICO          = r'&&'
t_OU_LOGICO         = r'\|\|'
t_NEGACAO           = r'\!'
t_ABRE_PARENTESE    = r'\('
t_FECHA_PARENTESE   = r'\)'
t_ABRE_COLCHETE     = r'\['
t_FECHA_COLCHETE    = r'\]'
t_SE                = r'se'
t_ENTAO             = r'entao'
t_SENAO             = r'senao'
t_FIM               = r'fim'
t_REPITA            = r'repita'
t_ATE               = r'ate'
t_LEIA              = r'leia'
t_ESCREVA           = r'escreva'
t_RETORNA           = r'retorna'
t_FUNCAO            = r'funcao'

#PALAVRAS RESERVADAS
reservadas = {
    'se'        : 'SE',
    'entao'     : 'ENTAO',
    'senao'     : 'SENAO',
    'fim'       : 'FIM',
    'repita'    : 'REPITA',
    'ate'       : 'ATE',
    'leia'      : 'LEIA',
    'escreva'   : 'ESCREVA',
    'retorna'   : 'RETORNA',
    'inteiro'   : 'INTEIRO',
    'flutuante' : 'FLUTUANTE',
}

##REGRAS COM ACAO
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_NUM_FLUTUANTE(t):
    r'\d+\.\d*'
    t.value = float(t.value)
    return t


def t_NUM_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

##ROTINA AUXILIAR
# Build the lexer
lexer = lex.lex()
# Test it out
data = ''' inteiro aba = 0
'''
# Give the lexer some input
lexer.input(data)
 
# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)   