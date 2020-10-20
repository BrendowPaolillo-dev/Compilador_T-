from sys import argv, exit

import ply.yacc as yacc
 
# Get the token map from the lexer.  This is required.
import sys
from lex import tokens, log
from anytree.exporter import UniqueDotExporter, DotExporter
from anytree import Node, RenderTree

tokens = tokens
error = False
root = None
id = 0

      
# Classe de nó
class MyNode(Node):
    def __init__(self, typeN,  parent = None, children = None):
        super(Node, self).__init__()
        global id
        self.name = str(typeN)
        self.id = id
        self.parent = parent
        if children:
            self.children = children
        # self.value = value 
        
            
        id += 1
    def __str__(self):  
        return (self.name)



# Verificar como utilizar a anytree. Tem um exportador Dot Graphviz.


# Sub-árvore.
#       (programa)
#           |
#   (lista_declaracoes)
#     /     |      \
#   ...    ...     ...


def p_programa(p):
    "programa : lista_declaracoes"
    global root
    p[0] = MyNode("programa", children = [p[1]])
    root = p[0]


def p_lista_declaracoes(p):
    """lista_declaracoes : lista_declaracoes declaracao
                        | declaracao
    """
    if len(p) > 2:
        p[0] = MyNode ('lista_declaracoes', children = [p[1], p[2]])
    else:
        p[0] = MyNode('lista_declaracoes', children = [p[1]])

def p_declaracao(p):
    """declaracao : declaracao_variaveis
                | inicializacao_variaveis
                | funcao
    """
    p[0] = MyNode('declaracao', children = [p[1]])
    
    

# Sub-árvore.
#      (declaracao_variaveis)
#      / p[1]    |           \
# (tipo)    (DOIS_PONTOS)    (lista_variaveis)
#                |
#               (:)

def p_declaracao_variaveis(p):
    "declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis"
    dp = MyNode("DOIS_PONTOS", children=[MyNode(p[2])])
    p[0] = MyNode('declaracao_variaveis', children=[p[1], dp, p[3]])

    

 

def p_inicializacao_variaveis(p):
    "inicializacao_variaveis : atribuicao"
    p[0] = MyNode('inicializacao_variaveis', children = [p[1]])
    

def p_lista_variaveis(p):
    """lista_variaveis : lista_variaveis VIRGULA var
                    | var
    """
    if len(p) == 4:
        p[0] = MyNode('lista_variaveis', children = [p[1], MyNode("VIRGULA", children=[MyNode(p[2])]),p[3]])
    else:
        p[0] = MyNode('lista_variaveis', children = [p[1]])

    
def p_var(p):
    """var : ID
        | ID indice
    """
    if len(p) == 3:
        p[0] = MyNode ('var', children = [MyNode("ID", children=[MyNode(p[1])]), p[2]])
    else:
        p[0] = MyNode('var', children = [MyNode("ID", children=[MyNode(p[1])])]) 


def p_indice(p):
    """indice : indice ABRE_COLCHETE expressao FECHA_COLCHETE
            | ABRE_COLCHETE expressao FECHA_COLCHETE
    """
    if len(p) == 5:
        p[0] = MyNode ('indice', children = [p[1], MyNode("ABRE_COLCHETE", children = [MyNode(p[2])]), p[3], MyNode("FECHA_COLCHETE", children = [MyNode(p[4])])])
    else:
        p[0] = MyNode('indice', children = [MyNode("ABRE_COLCHETE", children = [MyNode(p[1])]), p[2], MyNode("FECHA_COLCHETE", children = [MyNode(p[3])])])
    
    

def p_indice_error(p):
    """indice : ABRE_COLCHETE  error
            | error  FECHA_COLCHETE
            | ABRE_COLCHETE error FECHA_COLCHETE
            | indice ABRE_COLCHETE  error
            | indice error  FECHA_COLCHETE
            | indice ABRE_COLCHETE error FECHA_COLCHETE
    """
    if len(p) == 3:
        if str(p[2]) == "error":
            p[0] = MyNode ('indice_error', children = [MyNode("ABRE_COLCHETE", children = [MyNode(p[1])]), p[2]])
        else:
            p[0] = MyNode ('indice_error', children = [p[1], MyNode("FECHA_COLCHETE", children = [MyNode(p[2])])])
    elif len(p) == 4:
        if str(p[2]) == "error":
            p[0] = MyNode('indice_error', children = [MyNode("ABRE_COLCHETE", children = [MyNode(p[1])]), p[2], MyNode((p[3]))])
        elif str(p[3]) == "error":
            p[0] = MyNode('indice_error', children = [p[1], MyNode("ABRE_COLCHETE", children = [MyNode(p[2])]), p[3]]) 
        elif str(p[2]) == "error" and str(p[3]) == "FECHA_COLCHETE":
            p[0] = MyNode('indice_error', children = [p[1], p[2], MyNode("FECHA_COLCHETE", children = [MyNode(p[3])])]) 
    elif len(p) == 5:
        if str(p[3]) == 'error':
            p[0] = MyNode('indice_error', children = [p[1], MyNode("ABRE_COLCHETE", children = [MyNode(p[2])]), p[3], MyNode("FECHA_COLCHETE", children = [MyNode(p[4])])])
    
    
# Sub-árvore:
#    (tipo)
#      |
#  (FLUTUANTE)
def p_tipo(p):
    """tipo : INTEIRO
        | FLUTUANTE
    """
    if str(p[1]) == "inteiro":
        tipo = MyNode("INTEIRO", children = [MyNode(p[1])])
        p[0] = MyNode("tipo", children=[tipo])
    else:
        tipo = MyNode("FLUTUANTE", children = [MyNode(p[1])])
        p[0] = MyNode("tipo", children=[tipo])


def p_funcao(p):
    """funcao : tipo cabecalho 
                        | cabecalho 
    """
    if len(p) == 3:
        p[0] = MyNode ('funcao', children = [p[1], p[2]])
    else:
        p[0] = MyNode('funcao', children = [p[1]]) 
    
def p_cabecalho(p):
    """cabecalho : ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM
                |"""
    p[0] = MyNode('cabecalho', children = [MyNode("ID", children = [MyNode(p[1])]), MyNode("ABRE_PARENTESE", children = [MyNode(p[2])]), p[3], MyNode("FECHA_PARENTESE", children = [MyNode(p[4])]), p[5], MyNode("FIM", children = [MyNode(p[6])])])

def p_cabecalho_error(p):
    """cabecalho : ID error lista_parametros FECHA_PARENTESE corpo FIM
                | ID ABRE_PARENTESE lista_parametros error corpo FIM
                | ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo 
    """

    if len(p) == 7:
        if str(p[4]) == "error":
            p[0] = MyNode('cabecalho_error', children = [MyNode("ID", children = [MyNode(p[1])]), MyNode("ABRE_PARENTESE", children = [MyNode(p[2])]), p[3], p[4], p[5], MyNode("FIM", children = [MyNode(p[6])])]) 
        elif str(p[2]) == "error":
            p[0] = MyNode('cabecalho_error', children = [MyNode("ID", children = [MyNode(p[1])]), p[2], p[3], MyNode("FECHA_PARENTESE", children = [MyNode(p[4])]), p[5],  MyNode("FIM", children = [MyNode(p[6])])]) 
        elif str(p[6]) == "corpo":
            p[0] = MyNode('cabecalho_error', children = [MyNode("ID", children = [MyNode(p[1])]), MyNode("ABRE_PARENTESE", children = [MyNode(p[2])]), p[3], MyNode("FECHA_PARENTESE", children = [MyNode(p[4])]), p[5], p[6]]) 



def p_lista_parametros(p):
    """lista_parametros : lista_parametros VIRGULA parametro
                    | parametro
                    | vazio
    """
    if len(p) > 3 :
        p[0] = MyNode("lista_parametros", children = [p[1], MyNode("VIRGULA", children=[MyNode(p[2])]),p[3]])
    else:
        p[0] = MyNode("lista_parametros", children = [p[1]])

def p_parametro(p):
    """parametro : tipo DOIS_PONTOS ID
                | parametro ABRE_COLCHETE FECHA_COLCHETE
    """
    if str(p[1]) == "tipo":
        p[0] = MyNode("parametro", children = [p[1], MyNode("DOIS_PONTOS", children = [MyNode(p[2])]), MyNode("ID", children = [MyNode(p[3])])])
    else:
        p[0] = MyNode("parametro", children = [p[1], MyNode("ABRE_COLCHETE", children = [MyNode(p[2])]), MyNode("FECHA_COLCHETE", children = [MyNode(p[3])])])


def p_parametro_error(p):
    """parametro : tipo error ID
                | error ID
                | parametro error FECHA_COLCHETE
                | parametro ABRE_COLCHETE error
    """
    if len(p) == 3:
        if str(p[1]) == 'error':
            p[0] = MyNode("parametro_error", children = [p[1], MyNode(p[2].upper(), children = [MyNode(p[2])])])
    elif len(p) == 4:
        if str(p[2]) == "error":
            p[0] = MyNode("parametro_error", children = [p[1], p[2], MyNode(p[3].upper(), children = [MyNode(p[3])])])
        elif str(p[3]) == "error":
            p[0] = MyNode("parametro_error", children = [p[1], MyNode(p[2].upper(), children = [MyNode(p[2])]), p[3]])
        else:             
            p[0] = MyNode("parametro_error", children = [p[1], MyNode(p[2].upper(), children = [MyNode(p[2])]), p[3]])

def p_corpo(p):
    """corpo : corpo acao
            | vazio
    """
    if len(p) == 3:
        p[0] = MyNode("corpo", children = [p[1], p[2]])
    elif len(p) == 2: 
        p[0] = MyNode("corpo", children = [p[1]])


def p_acao(p):
    """acao : expressao
        | declaracao_variaveis
        | se
        | repita
        | leia
        | escreva
        | retorna
    """
    p[0] = MyNode("acao", children= [MyNode(p[1])])

def p_se_error(p):
    """se : error expressao ENTAO corpo FIM
        | SE expressao error corpo FIM
        | error expressao ENTAO corpo SENAO corpo FIM
        | SE expressao error corpo SENAO corpo FIM
        | SE expressao ENTAO corpo error corpo FIM
        | SE expressao ENTAO corpo SENAO corpo
    """
    if len(p) == 6:
        if str(p[1]) == "error":
            p[0] = MyNode("se_error", children = [p[1], p[2], MyNode((p[3])), p[4], MyNode((p[5]))])
        elif str(p[3]) == "error":             
            p[0] = MyNode("se_error", children = [MyNode((p[1])), p[2], p[3], p[4], MyNode((p[5]))])
            
    elif len(p) == 7:
        p[0] = MyNode("se_error", children = [MyNode((p[1])), p[2], MyNode((p[3])), p[4], MyNode((p[5])), p[6]])
    
    elif len(p) == 8:
        if str(p[1]) == 'error':
            p[0] = MyNode("se_error", children = [p[1], p[2], MyNode((p[3])), p[4], MyNode((p[5])), p[6], MyNode((p[7]))])
        elif str(p[3]) == "error":
            p[0] = MyNode("se_error", children = [MyNode((p[1])), p[2], MyNode((p[3])), p[4], p[5], p[6], MyNode((p[7]))])
        elif str(p[5]) == "error":             
            p[0] = MyNode("se_error", children = [MyNode((p[1])), p[2], p[3], p[4], MyNode((p[5])), p[6], MyNode((p[7]))])
        
    
# Sub-árvore:
#           ___ (SE) ____
#          /      |      \
# (expressao)  (entao)  (senao)
              
def p_se(p):
    """se : SE expressao ENTAO corpo FIM
        | SE expressao ENTAO corpo SENAO corpo FIM
    """
    if str(p[5]) == 'FIM':
        p[0] = MyNode('se', children=[MyNode("SE", children = [MyNode(p[1])]), p[2], MyNode("ENTAO", children = [MyNode(p[3])]), p[4], MyNode("FIM", children = [MyNode(p[5])])])
    elif str(p[5]) == 'SENAO':
        p[0] = MyNode('se', children=[MyNode("SE", children = [MyNode(p[1])]), p[2],  MyNode("ENTAO", children = [MyNode(p[3])]), p[4], MyNode("SENAO", children = [MyNode(p[5])]), p[6],  MyNode("FIM", children = [MyNode(p[7])])])
             
def p_repita(p):
    "repita : REPITA corpo ATE expressao"
    p[0] = MyNode('repita', children=[MyNode("REPITA", children=[MyNode(p[1])]), p[2], MyNode("ATE", children=[MyNode(p[3])]), p[4]])

def p_repita_error(p):
    """repita : error corpo ATE expressao
            | REPITA corpo error expressao
    """
    if str(p[1]) == 'error':
        p[0] = MyNode('repita_error', children=[p[1], p[2], MyNode("REPITA", children=[MyNode(p[3])]), p[4]])
    elif str(p[3]) == 'error':
        p[0] = MyNode('repita_error', children=[MyNode("REPITA", children=[MyNode(p[1])]), p[2], p[3], p[4]])
 

def p_atribuicao(p):
    """atribuicao : var ATRIBUICAO expressao"""

    p[0] = MyNode('atribuicao', children=[p[1], MyNode("ATRIBUICAO", children = [MyNode(p[2])]), p[3]])

def p_leia(p):
    "leia : LEIA ABRE_PARENTESE var FECHA_PARENTESE"
    p[0] = MyNode('leia', children=[MyNode("LEIA", children = [MyNode(p[1])]), MyNode("ABRE_PARENTESE", children = [MyNode(p[2])]), p[3], MyNode("FECHA_PARENTESE", children = [MyNode(p[4])])])


def p_leia_error(p):
    """leia : LEIA ABRE_PARENTESE error FECHA_PARENTESE
    """
    p[0] = MyNode('leia', children=[MyNode("LEIA", children = [MyNode(p[1])]), MyNode("ABRE_PARENTESE", children = [MyNode(p[2])]), p[3], MyNode("FECHA_PARENTESE", children = [MyNode(p[4])])])

    
def p_escreva(p):
    "escreva : ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESE"
    p[0] = MyNode('escreva', children=[MyNode("ESCREVA", children = [MyNode(p[1])]), MyNode("ABRE_PARENTESE", children = [MyNode(p[2])]), p[3], MyNode("FECHA_PARENTESE", children = [MyNode(p[4])])])




def p_retorna(p):
    "retorna : RETORNA ABRE_PARENTESE expressao FECHA_PARENTESE"
    p[0] = MyNode('retorna', children=[MyNode("RETORNA", children = [MyNode(p[1])]), MyNode("ABRE_PARENTESE", children = [MyNode(p[2])]), p[3], MyNode("FECHA_PARENTESE", children = [MyNode(p[4])])])




def p_expressao(p):
    """expressao : expressao_logica
                | atribuicao
    """
    p[0] = MyNode('expressao', children=[p[1]])


def p_expressao_logica(p):
    """expressao_logica : expressao_simples
                    | expressao_logica operador_logico expressao_simples
    """
    if len(p) > 3:
        p[0] = MyNode('expressao_logica', children=[p[1], p[2], p[3]])
    else:
        p[0] = MyNode('expressao_logica', children=[p[1]])
        
def p_expressao_simples(p):
    """expressao_simples : expressao_aditiva
                        | expressao_simples operador_relacional expressao_aditiva
    """
    if len(p) > 3:
        p[0] = MyNode('expressao_simples', children=[p[1], p[2], p[3]])
    else:
        p[0] = MyNode('expressao_simples', children=[p[1]])
        
def p_expressao_aditiva(p):
    """expressao_aditiva : expressao_multiplicativa
                        | expressao_aditiva operador_soma expressao_multiplicativa
    """
    if len(p) > 3:
        p[0] = MyNode('expressao_aditiva', children=[p[1], p[2], p[3]])
    else:
        p[0] = MyNode('expressao_aditiva', children=[p[1]])

def p_expressao_multiplicativa(p):
    """expressao_multiplicativa : expressao_unaria
                               | expressao_multiplicativa operador_multiplicacao expressao_unaria
        """
    if len(p) > 3:
        p[0] = MyNode('expressao_multiplicativa', children=[p[1], p[2], p[3]])
    else:
        p[0] = MyNode('expressao_multiplicativa', children=[p[1]])

def p_expressao_unaria(p):
    """expressao_unaria : fator
                        | operador_soma fator
                        | operador_negacao fator
        """
    if len(p) > 2:
        p[0] = MyNode('expressao_unaria', children=[p[1], p[2]])
    else:
        p[0] = MyNode('expressao_unaria', children=[p[1]])


def p_operador_relacional(p):
    """operador_relacional : MENOR
                            | MAIOR
                            | IGUAL
                            | DIFERENTE 
                            | MENOR_IGUAL
                            | MAIOR_IGUAL
    """
    p[0] = MyNode('operador_relacional', children=[MyNode(p[1].upper(), children = [MyNode(p[1])])])

def p_operador_soma(p):
    """operador_soma : MAIS
                    | MENOS
    """
    p[0] = MyNode('operador_soma', children=[MyNode(p[1].upper(), children = [MyNode(p[1])])])


def p_operador_logico(p):
    """operador_logico : E_LOGICO
                    | OU_LOGICO
    """
    p[0] = MyNode('operador_logico', children=[MyNode(p[1].upper(), children = [MyNode(p[1])])])


def p_operador_negacao(p):
    "operador_negacao : NEGACAO"
    p[0] = MyNode('operador_negacao', children=[MyNode(p[1].upper(), children = [MyNode(p[1])])])


def p_operador_multiplicacao(p):
    """operador_multiplicacao : MULTIPLICACAO
                            | DIVISAO
        """
    p[0] = MyNode('operador_multiplicacao', children=[MyNode(p[1].upper(), children = [MyNode(p[1])])])

def p_fator(p):
    """fator : ABRE_PARENTESE expressao FECHA_PARENTESE
            | var
            | chamada_funcao
            | numero
        """
    if len(p) > 3:
        p[0] = MyNode('fator', children=[MyNode("ABRE_PARENTESE",children=[MyNode(p[1])]), p[2], MyNode("FECHA_PARENTESE",children=[MyNode(p[3])])])
    else:
        p[0] = MyNode('fator', children=[p[1]])

def p_fator_error(p):
    """fator : ABRE_PARENTESE expressao 
    """
    p[0] = MyNode('fator_error', children=[MyNode((p[1])), p[2]])

def p_numero(p):
    """numero : NUM_INTEIRO
            | NUM_PONTO_FLUTUANTE
            | NUM_NOTACAO_CIENTIFICA
        """
    if type(p[1]) == int:
        p[0] = MyNode('numero', children=[MyNode("NUM_INTEIRO", children =[MyNode(p[1])])])
    elif type(p[1]) == float:
        p[0] = MyNode('numero', children=[MyNode("NUM_PONTO_FLUTUANTE", children =[MyNode(p[1])])])
    else:
        p[0] = MyNode('numero', children=[MyNode("NUM_NOTACAO_CIENTIFICA", children =[MyNode(p[1])])])        

def p_chamada_funcao(p):
    "chamada_funcao : ID ABRE_PARENTESE lista_argumentos FECHA_PARENTESE"
    p[0] = MyNode('chamada_funcao', children = [MyNode("ID", children = [MyNode(p[1])]), MyNode("ABRE_PARENTESE", children = [MyNode(p[2])]), p[3], MyNode("FECHA_PARENTESE", children = [MyNode(p[4])])])


def p_lista_argumentos(p):
    """lista_argumentos : lista_argumentos VIRGULA expressao
                    | expressao
                    | vazio
        """
    if len(p) > 3:
        p[0] = MyNode("lista_argumentos", children = [p[1], MyNode("VIRGULA", children=[MyNode(p[2])]),p[3]])
    else:
        p[0] = MyNode('lista_argumentos', children=[p[1]])

def p_vazio(p):
    "vazio : "
    p[0] = MyNode('vazio')

def find_column(token):
    input = token.lexer.lexdata
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def p_error(p):
    global error 

    if p:
        token = p
        print("['{line}','{column}']: erro próximo ao token '{token}'".format(line=token.lineno, column=find_column(p), token=token.value))
    else:
        print("Syntax error at EOF")
    error = True
    
# Programa principal.
def main():
    global root

    aux = argv[1].split('.')
    if aux[-1] != 'tpp':
      raise IOError("Not a .tpp file!")
    data = open(argv[1])

    source_file = data.read()
    root = parser.parse(source_file)

    if root and root.children != ():
        print('\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n')
        print("Generating AST, please waiexport_ASTt...")
        UniqueDotExporter(root).to_picture("unique.tree.png")
        UniqueDotExporter(root).to_dotfile("unique.tree.dot")
        print("AST was successfully generated.\nOutput file: 'tree.png'")
    else:
        log .error("Unable to generate AST -- Syntax nodes not found")
    print('\n\n')

# Build the parser.
parser = yacc.yacc(optimize=True, start='programa',debug=True,debuglog=log)

if __name__ == "__main__":
    main()