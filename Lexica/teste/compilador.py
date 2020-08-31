import ply.lex as lex

tokens = (
    "MAIS",
    "MENOS",
    "MULTIPLICACAO",
    "DIVISAO",
    "DOIS_PONTOS",
    "VIRGULA",
    "MENOR",
    "MAIOR",
    "IGUAL",
    "DIFERENTE",
    "MENOR_IGUAL",
    "MAIOR_IGUAL",
    "E_LOGICO",
    "OU_LOGICO",
    "NEGACAO",
    "ABRE_PARENTESE",
    "FECHA_PARENTESE",
    "ABRE_COLCHETE",
    "FECHA_COLCHETE",
    "SE",
    "ENTAO",
    "SENAO",
    "FIM",
    "REPITA",
    "ATE",
    "ATRIBUICAO",
    "LEIA",
    "ESCREVA",
    "RETORNA",
    "INTEIRO",
    "FLUTUANTE",
    "NUM_INTEIRO",
    "NUM_PONTO_FLUTUANTE",
    "NUM_NOTACAO_CIENTIFICA",
    "ID",
)

t_MAIS = r"\+"
t_MENOS = r"-"
t_MULTIPLICACAO = r"\*"
t_DIVISAO = r"/"
t_DOIS_PONTOS = r":"
t_VIRGULA = r","
t_MENOR = r"<"
t_MAIOR = r">"
t_IGUAL = r"=="
t_DIFERENTE = r"<>"
t_MENOR_IGUAL = r"<="
t_MAIOR_IGUAL = r">="
t_E_LOGICO = r"&&"
t_OU_LOGICO = r"||"
t_NEGACAO = r"!"
t_ABRE_PARENTESE = r"\("
t_FECHA_PARENTESE = r"\)"
t_ABRE_COLCHETE = r"\["
t_FECHA_COLCHETE = r"\]"
t_SE = r"se"
t_ENTAO = r"então"
t_SENAO = r"senão"
t_FIM = r"fim"
t_REPITA = r"repita"
t_ATE = r"até"
t_ATRIBUICAO = r":="
t_LEIA = r"leia"
t_ESCREVA = r"escreva"
t_RETORNA = r"retorna"
t_INTEIRO = r"inteiro"
t_FLUTUANTE = r"flutuante"
t_NUM_INTEIRO = r"\d+"
t_NUM_PONTO_FLUTUANTE = r"(+|-)?\d+\.?\d*"
t_NUM_NOTACAO_CIENTIFICA = r"(+|-)?\d+\.?\d*e(+|-)?\d+\.?\d*"
t_ID = r"id"

lexer = lex.lex()