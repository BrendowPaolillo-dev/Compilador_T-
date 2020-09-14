#------------------------------------------------------------
# lex.py
#
# Analisador lexico
# Brendow Paolillo Castro Isidoro
# ------------------------------------------------------------
import ply.lex as lex
import os

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
    'ABRE_CHAVE',
    'FECHA_CHAVE',
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
t_ABRE_CHAVE        = r'\{'
t_FECHA_CHAVE       = r'\}'
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

#Define um ID como uma sequencia de qualquer caractere alfabético, 
#seguido de qualquer quantidade sequências de caracteres
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

#Define um valor de ponto flutuante
def t_NUM_PONTO_FLUTUANTE(t):
    r'\d+\.\d*'
    t.value = float(t.value)
    return t

#Define um valor inteiro
def t_NUM_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

#Descreve uma nova linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorando espaços em brancos, podendo ser espaços ou tabulações
t_ignore  = ' \t'

# Lidando com erros
def t_error(t):
    print("Caractere nao aceito '%s'" % t.value[0])
    t.lexer.skip(1)

def verify_input():
    while True:
        response = (str(input()))
        print ((response))
        if response == "":
            break

def show_all_tokens():
    print("Imprimindo a lista de tokens:\n")
    for x in tokens:
        print(str(x))
    print("\nAperte enter para continuar com os testes...")
    verify_input()

##ROTINA AUXILIAR
# Contruindo o lexer
lexer = lex.lex()

show_all_tokens()

# Realizando a leitura do arquivo`
for data_name in sorted(os.listdir("./Lexica/lexica-testes/")):
    print ("Realizando o teste do arquivo: " + str(data_name) + '\n')
    data = open("./Lexica/lexica-testes/" + str(data_name), 'r')

# Entrando com arquivo no lexer
    lexer.input(data.read())

 
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # Quando não tiver mais token para realizar a analise
        print(tok.type, tok.value, tok.lineno, tok.lexpos)
        
    print("\nAperte enter para realizar o próximo teste...")
    verify_input()