# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('ABRE_COLCHETE', 'ABRE_PARENTESE', 'ATE', 'ATRIBUICAO', 'DIFERENCA', 'DIVISAO', 'DOIS_PONTOS', 'ENTAO', 'ESCREVA', 'E_LOGICO', 'FECHA_COLCHETE', 'FECHA_PARENTESE', 'FIM', 'FLUTUANTE', 'ID', 'IGUAL', 'INTEIRO', 'LEIA', 'MAIOR', 'MAIOR_IGUAL', 'MAIS', 'MENOR', 'MENOR_IGUAL', 'MENOS', 'MULTIPLICACAO', 'NEGACAO', 'NUM_INTEIRO', 'NUM_NOTACAO_CIENTIFICA', 'NUM_PONTO_FLUTUANTE', 'OU_LOGICO', 'REPITA', 'RETORNA', 'SE', 'SENAO', 'VIRGULA'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_ID>(([a-zA-ZáÁãÃàÀéÉíÍóÓõÕ])(([0-9])+|_|([a-zA-ZáÁãÃàÀéÉíÍóÓõÕ]))*))|(?P<t_NUM_NOTACAO_CIENTIFICA>(([\\-\\+]?)([1-9])\\.([0-9])+[eE]([\\-\\+]?)([0-9])+))|(?P<t_NUM_PONTO_FLUTUANTE>(([0-9])+\\.([0-9])*))|(?P<t_NUM_INTEIRO>\\d+)|(?P<t_COMENTARIO>(\\{((.|\\n)*?)\\}))|(?P<t_newline>\\n+)|(?P<t_OU_LOGICO>\\|\\|)|(?P<t_MAIS>\\+)|(?P<t_MULTIPLICACAO>\\*)|(?P<t_ABRE_PARENTESE>\\()|(?P<t_FECHA_PARENTESE>\\))|(?P<t_ABRE_COLCHETE>\\[)|(?P<t_FECHA_COLCHETE>\\])|(?P<t_ATRIBUICAO>:=)|(?P<t_E_LOGICO>&&)|(?P<t_DIFERENCA><>)|(?P<t_MENOR_IGUAL><=)|(?P<t_MAIOR_IGUAL>>=)|(?P<t_MENOS>-)|(?P<t_DIVISAO>/)|(?P<t_VIRGULA>,)|(?P<t_DOIS_PONTOS>:)|(?P<t_NEGACAO>!)|(?P<t_MENOR><)|(?P<t_MAIOR>>)|(?P<t_IGUAL>=)', [None, ('t_ID', 'ID'), None, None, None, None, None, ('t_NUM_NOTACAO_CIENTIFICA', 'NUM_NOTACAO_CIENTIFICA'), None, None, None, None, None, None, ('t_NUM_PONTO_FLUTUANTE', 'NUM_PONTO_FLUTUANTE'), None, None, None, ('t_NUM_INTEIRO', 'NUM_INTEIRO'), ('t_COMENTARIO', 'COMENTARIO'), None, None, None, ('t_newline', 'newline'), (None, 'OU_LOGICO'), (None, 'MAIS'), (None, 'MULTIPLICACAO'), (None, 'ABRE_PARENTESE'), (None, 'FECHA_PARENTESE'), (None, 'ABRE_COLCHETE'), (None, 'FECHA_COLCHETE'), (None, 'ATRIBUICAO'), (None, 'E_LOGICO'), (None, 'DIFERENCA'), (None, 'MENOR_IGUAL'), (None, 'MAIOR_IGUAL'), (None, 'MENOS'), (None, 'DIVISAO'), (None, 'VIRGULA'), (None, 'DOIS_PONTOS'), (None, 'NEGACAO'), (None, 'MENOR'), (None, 'MAIOR'), (None, 'IGUAL')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
