
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_CHAVE ABRE_COLCHETE ABRE_PARENTESE ATE ATE ATRIBUICAO COMENTARIO DIFERENTE DIVISAO DOIS_PONTOS ENTAO ENTAO ESCREVA ESCREVA E_LOGICO FECHA_CHAVE FECHA_COLCHETE FECHA_PARENTESE FIM FIM FLUTUANTE FLUTUANTE FUNCAO ID IGUAL INTEIRO INTEIRO LEIA LEIA MAIOR MAIOR_IGUAL MAIS MENOR MENOR_IGUAL MENOS MULTIPLICACAO NEGACAO NUM_INTEIRO NUM_NOTACAO_CIENTIFICA NUM_PONTO_FLUTUANTE OU_LOGICO REPITA REPITA RETORNA RETORNA SE SE SENAO SENAO VIRGULAprograma : lista_declaracoeslista_declaracoes : lista_declaracoes declaracao\n                        | declaracao\n    declaracao : declaracao_variaveis\n                | inicializacao_variaveis\n                | funcao\n    declaracao_variaveis : tipo DOIS_PONTOS lista_variaveisinicializacao_variaveis : atribuicaolista_variaveis : lista_variaveis VIRGULA var\n                    | var\n    var : ID\n        | ID indice\n    indice : indice ABRE_COLCHETE expressao FECHA_COLCHETE\n            | ABRE_COLCHETE expressao FECHA_COLCHETE\n    indice : ABRE_COLCHETE  error\n            | error  FECHA_COLCHETE\n            | ABRE_COLCHETE error FECHA_COLCHETE\n            | indice ABRE_COLCHETE  error\n            | indice error  FECHA_COLCHETE\n            | indice ABRE_COLCHETE error FECHA_COLCHETE\n    tipo : INTEIRO\n        | FLUTUANTE\n    funcao : tipo cabecalho \n                        | cabecalho \n    cabecalho : ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM\n                |cabecalho : ID error lista_parametros FECHA_PARENTESE corpo FIM\n                | ID ABRE_PARENTESE lista_parametros error corpo FIM\n                | ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo \n    lista_parametros : lista_parametros VIRGULA parametro\n                    | parametro\n                    | vazio\n    parametro : tipo DOIS_PONTOS ID\n                | parametro ABRE_COLCHETE FECHA_COLCHETE\n    parametro : tipo error ID\n                | error ID\n                | parametro error FECHA_COLCHETE\n                | parametro ABRE_COLCHETE error\n    corpo : corpo acao\n            | vazio\n    acao : expressao\n        | declaracao_variaveis\n        | se\n        | repita\n        | leia\n        | escreva\n        | retorna\n    se : error expressao ENTAO corpo FIM\n        | SE expressao error corpo FIM\n        | error expressao ENTAO corpo SENAO corpo FIM\n        | SE expressao error corpo SENAO corpo FIM\n        | SE expressao ENTAO corpo error corpo FIM\n        | SE expressao ENTAO corpo SENAO corpo\n    se : SE expressao ENTAO corpo FIM\n        | SE expressao ENTAO corpo SENAO corpo FIM\n    repita : REPITA corpo ATE expressaorepita : error corpo ATE expressao\n            | REPITA corpo error expressao\n    atribuicao : var ATRIBUICAO expressaoleia : LEIA ABRE_PARENTESE var FECHA_PARENTESEleia : LEIA ABRE_PARENTESE error FECHA_PARENTESE\n    escreva : ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESEretorna : RETORNA ABRE_PARENTESE expressao FECHA_PARENTESEexpressao : expressao_logica\n                | atribuicao\n    expressao_logica : expressao_simples\n                    | expressao_logica operador_logico expressao_simples\n    expressao_simples : expressao_aditiva\n                        | expressao_simples operador_relacional expressao_aditiva\n    expressao_aditiva : expressao_multiplicativa\n                        | expressao_aditiva operador_soma expressao_multiplicativa\n    expressao_multiplicativa : expressao_unaria\n                               | expressao_multiplicativa operador_multiplicacao expressao_unaria\n        expressao_unaria : fator\n                        | operador_soma fator\n                        | operador_negacao fator\n        operador_relacional : MENOR\n                            | MAIOR\n                            | IGUAL\n                            | DIFERENTE \n                            | MENOR_IGUAL\n                            | MAIOR_IGUAL\n    operador_soma : MAIS\n                    | MENOS\n    operador_logico : E_LOGICO\n                    | OU_LOGICO\n    operador_negacao : NEGACAOoperador_multiplicacao : MULTIPLICACAO\n                            | DIVISAO\n        fator : ABRE_PARENTESE expressao FECHA_PARENTESE\n            | var\n            | chamada_funcao\n            | numero\n        fator : ABRE_PARENTESE expressao \n    numero : NUM_INTEIRO\n            | NUM_PONTO_FLUTUANTE\n            | NUM_NOTACAO_CIENTIFICA\n        chamada_funcao : ID ABRE_PARENTESE lista_argumentos FECHA_PARENTESElista_argumentos : lista_argumentos VIRGULA expressao\n                    | expressao\n                    | vazio\n        vazio : '
    
_lr_action_items = {'INTEIRO':([0,2,3,4,5,6,7,8,9,10,11,14,16,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,80,81,82,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,117,118,119,120,121,122,123,124,125,127,129,133,134,137,139,143,145,146,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[10,10,-3,-4,-5,-6,-26,-8,-24,-21,-22,-2,-23,10,10,-12,-7,-10,-11,10,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-102,-102,10,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,10,-40,10,10,-13,-20,-98,-25,-39,-41,-42,-43,-44,-45,-46,-47,-102,-102,-28,-27,10,10,-102,-102,-102,-102,10,-57,10,10,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,-102,-54,-102,10,10,10,10,-50,-51,-52,-55,]),'FLUTUANTE':([0,2,3,4,5,6,7,8,9,10,11,14,16,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,80,81,82,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,117,118,119,120,121,122,123,124,125,127,129,133,134,137,139,143,145,146,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[11,11,-3,-4,-5,-6,-26,-8,-24,-21,-22,-2,-23,11,11,-12,-7,-10,-11,11,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-102,-102,11,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,11,-40,11,11,-13,-20,-98,-25,-39,-41,-42,-43,-44,-45,-46,-47,-102,-102,-28,-27,11,11,-102,-102,-102,-102,11,-57,11,11,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,-102,-54,-102,11,11,11,11,-50,-51,-52,-55,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,14,15,16,18,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,54,55,58,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,116,117,118,119,120,121,122,123,124,125,127,128,129,133,134,137,139,140,141,142,143,144,145,146,147,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[13,13,-3,-4,-5,-6,17,-8,-24,-21,-22,-2,25,-23,33,-12,33,-7,-10,-11,-91,-59,-64,-65,-66,-68,-11,-70,33,-72,-74,33,33,-92,-93,-83,-84,-87,-95,-96,-97,83,-16,33,-15,25,33,-85,-86,33,-77,-78,-79,-80,-81,-82,33,33,33,-88,-89,-75,-91,-76,-94,-102,-102,110,111,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,33,-40,33,33,-13,-20,-98,33,-25,-39,-41,-42,-43,-44,-45,-46,-47,33,33,-102,-28,-27,33,33,25,33,33,-102,33,-102,-102,33,33,33,-57,33,33,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,33,-54,-102,33,33,33,33,-50,-51,-52,-55,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,14,16,21,23,24,25,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,80,90,91,92,93,94,95,96,97,101,102,103,104,113,114,115,117,118,119,120,121,122,123,124,125,133,134,154,157,158,159,160,161,162,163,165,168,169,173,174,175,176,177,],[-26,0,-1,-3,-4,-5,-6,-26,-8,-24,-21,-22,-2,-23,-12,-7,-10,-11,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,-29,-40,-13,-20,-98,-25,-39,-41,-42,-43,-44,-45,-46,-47,-28,-27,-57,-56,-58,-60,-61,-62,-63,-48,-49,-54,-102,-53,-50,-51,-52,-55,]),'DOIS_PONTOS':([7,10,11,52,126,],[15,-21,-22,86,15,]),'error':([10,11,13,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,48,50,51,52,54,55,58,76,77,78,79,80,81,82,83,84,88,90,91,92,93,94,95,96,97,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,118,119,120,121,122,123,124,125,127,129,137,138,139,140,143,145,146,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[-21,-22,20,26,49,49,56,58,-7,-10,60,49,-91,-59,-64,-65,-66,-68,60,-70,-72,-74,-92,-93,-95,-96,-97,81,85,-32,87,-16,90,-15,-75,-91,-76,-94,-102,-102,49,-36,108,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,127,-40,127,85,-34,-38,-37,-33,-35,127,-13,-20,-98,-39,-41,-42,-43,-44,-45,-46,-47,-102,-102,127,145,148,150,-102,-102,-102,-102,127,-57,127,167,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,-102,-54,-102,127,127,127,127,-50,-51,-52,-55,]),'ATRIBUICAO':([12,13,21,27,33,54,58,90,91,92,93,113,114,],[18,-11,-12,18,-11,-16,-15,-18,-19,-14,-17,-13,-20,]),'ABRE_PARENTESE':([13,17,18,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,54,55,58,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,116,118,119,120,121,122,123,124,125,127,128,129,130,131,132,137,139,141,142,143,144,145,146,147,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[19,19,39,-12,39,-7,-10,-11,-91,-59,-64,-65,-66,-68,72,-70,39,-72,-74,39,39,-92,-93,-83,-84,-87,-95,-96,-97,-16,39,-15,39,-85,-86,39,-77,-78,-79,-80,-81,-82,39,39,39,-88,-89,-75,-91,-76,-94,-102,-102,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,39,-40,39,39,-13,-20,-98,39,-39,-41,-42,-43,-44,-45,-46,-47,39,39,-102,140,141,142,39,39,39,39,-102,39,-102,-102,39,39,39,-57,39,39,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,39,-54,-102,39,39,39,39,-50,-51,-52,-55,]),'ABRE_COLCHETE':([13,21,25,33,50,54,58,83,90,91,92,93,106,107,108,109,110,111,113,114,],[22,55,22,22,84,-16,-15,-36,-18,-19,-14,-17,84,-34,-38,-37,-33,-35,-13,-20,]),'MAIS':([18,21,22,23,24,25,27,28,29,30,31,32,33,34,36,37,39,40,41,42,43,45,46,47,54,55,58,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,116,118,119,120,121,122,123,124,125,127,128,129,137,139,141,142,143,144,145,146,147,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[42,-12,42,-7,-10,-11,-91,-59,-64,-65,-66,42,-11,-70,-72,-74,42,-92,-93,-83,-84,-95,-96,-97,-16,42,-15,42,-85,-86,42,-77,-78,-79,-80,-81,-82,42,42,42,-88,-89,-75,-91,-76,-94,-102,-102,-102,-18,-19,-14,-17,-9,-67,42,-71,-73,-90,42,-40,42,42,-13,-20,-98,42,-39,-41,-42,-43,-44,-45,-46,-47,42,42,-102,42,42,42,42,-102,42,-102,-102,42,42,42,-57,42,42,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,42,-54,-102,42,42,42,42,-50,-51,-52,-55,]),'MENOS':([18,21,22,23,24,25,27,28,29,30,31,32,33,34,36,37,39,40,41,42,43,45,46,47,54,55,58,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,116,118,119,120,121,122,123,124,125,127,128,129,137,139,141,142,143,144,145,146,147,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[43,-12,43,-7,-10,-11,-91,-59,-64,-65,-66,43,-11,-70,-72,-74,43,-92,-93,-83,-84,-95,-96,-97,-16,43,-15,43,-85,-86,43,-77,-78,-79,-80,-81,-82,43,43,43,-88,-89,-75,-91,-76,-94,-102,-102,-102,-18,-19,-14,-17,-9,-67,43,-71,-73,-90,43,-40,43,43,-13,-20,-98,43,-39,-41,-42,-43,-44,-45,-46,-47,43,43,-102,43,43,43,43,-102,43,-102,-102,43,43,43,-57,43,43,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,43,-54,-102,43,43,43,43,-50,-51,-52,-55,]),'NEGACAO':([18,21,22,23,24,25,27,28,29,30,31,32,33,34,36,37,39,40,41,42,43,45,46,47,54,55,58,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,116,118,119,120,121,122,123,124,125,127,128,129,137,139,141,142,143,144,145,146,147,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[44,-12,44,-7,-10,-11,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,44,-92,-93,-83,-84,-95,-96,-97,-16,44,-15,44,-85,-86,44,-77,-78,-79,-80,-81,-82,44,44,44,-88,-89,-75,-91,-76,-94,-102,-102,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,44,-40,44,44,-13,-20,-98,44,-39,-41,-42,-43,-44,-45,-46,-47,44,44,-102,44,44,44,44,-102,44,-102,-102,44,44,44,-57,44,44,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,44,-54,-102,44,44,44,44,-50,-51,-52,-55,]),'NUM_INTEIRO':([18,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,54,55,58,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,116,118,119,120,121,122,123,124,125,127,128,129,137,139,141,142,143,144,145,146,147,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[45,-12,45,-7,-10,-11,-91,-59,-64,-65,-66,-68,-11,-70,45,-72,-74,45,45,-92,-93,-83,-84,-87,-95,-96,-97,-16,45,-15,45,-85,-86,45,-77,-78,-79,-80,-81,-82,45,45,45,-88,-89,-75,-91,-76,-94,-102,-102,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,45,-40,45,45,-13,-20,-98,45,-39,-41,-42,-43,-44,-45,-46,-47,45,45,-102,45,45,45,45,-102,45,-102,-102,45,45,45,-57,45,45,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,45,-54,-102,45,45,45,45,-50,-51,-52,-55,]),'NUM_PONTO_FLUTUANTE':([18,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,54,55,58,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,116,118,119,120,121,122,123,124,125,127,128,129,137,139,141,142,143,144,145,146,147,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[46,-12,46,-7,-10,-11,-91,-59,-64,-65,-66,-68,-11,-70,46,-72,-74,46,46,-92,-93,-83,-84,-87,-95,-96,-97,-16,46,-15,46,-85,-86,46,-77,-78,-79,-80,-81,-82,46,46,46,-88,-89,-75,-91,-76,-94,-102,-102,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,46,-40,46,46,-13,-20,-98,46,-39,-41,-42,-43,-44,-45,-46,-47,46,46,-102,46,46,46,46,-102,46,-102,-102,46,46,46,-57,46,46,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,46,-54,-102,46,46,46,46,-50,-51,-52,-55,]),'NUM_NOTACAO_CIENTIFICA':([18,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,54,55,58,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,116,118,119,120,121,122,123,124,125,127,128,129,137,139,141,142,143,144,145,146,147,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[47,-12,47,-7,-10,-11,-91,-59,-64,-65,-66,-68,-11,-70,47,-72,-74,47,47,-92,-93,-83,-84,-87,-95,-96,-97,-16,47,-15,47,-85,-86,47,-77,-78,-79,-80,-81,-82,47,47,47,-88,-89,-75,-91,-76,-94,-102,-102,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,47,-40,47,47,-13,-20,-98,47,-39,-41,-42,-43,-44,-45,-46,-47,47,47,-102,47,47,47,47,-102,47,-102,-102,47,47,47,-57,47,47,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,47,-54,-102,47,47,47,47,-50,-51,-52,-55,]),'FECHA_PARENTESE':([19,20,21,25,26,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,48,50,51,53,54,58,72,76,77,78,79,83,90,91,92,93,95,96,97,98,99,100,101,102,106,107,108,109,110,111,113,114,115,135,149,150,151,152,],[-102,-102,-12,-11,-102,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,80,-31,-32,88,-16,-15,-102,-75,-91,-76,102,-36,-18,-19,-14,-17,-67,-69,-71,115,-100,-101,-73,-90,-30,-34,-38,-37,-33,-35,-13,-20,-98,-99,159,160,161,162,]),'VIRGULA':([19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,48,50,51,53,54,58,72,76,77,78,79,83,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,109,110,111,113,114,115,135,],[-102,-102,-12,59,-10,-11,-102,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,82,-31,-32,82,-16,-15,-102,-75,-91,-76,-94,-36,-18,-19,-14,-17,-9,-67,-69,-71,116,-100,-101,-73,-90,-30,-34,-38,-37,-33,-35,-13,-20,-98,-99,]),'FECHA_COLCHETE':([20,21,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,56,57,58,60,76,77,78,79,84,85,89,90,91,92,93,95,96,97,101,102,113,114,115,],[54,-12,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,91,92,93,54,-75,-91,-76,-94,107,109,113,114,-19,-14,-17,-67,-69,-71,-73,-90,-13,-20,-98,]),'FIM':([21,23,24,25,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,80,81,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,118,119,120,121,122,123,124,125,143,145,146,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[-12,-7,-10,-11,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-102,-102,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,117,-40,133,134,-13,-20,-98,-39,-41,-42,-43,-44,-45,-46,-47,-102,-102,-102,163,-57,165,168,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,-102,-54,-102,174,175,176,177,-50,-51,-52,-55,]),'SE':([21,23,24,25,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,80,81,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,118,119,120,121,122,123,124,125,127,129,137,139,143,145,146,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[-12,-7,-10,-11,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-102,-102,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,128,-40,128,128,-13,-20,-98,-39,-41,-42,-43,-44,-45,-46,-47,-102,-102,128,128,-102,-102,-102,-102,128,-57,128,128,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,-102,-54,-102,128,128,128,128,-50,-51,-52,-55,]),'REPITA':([21,23,24,25,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,80,81,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,118,119,120,121,122,123,124,125,127,129,137,139,143,145,146,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[-12,-7,-10,-11,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-102,-102,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,129,-40,129,129,-13,-20,-98,-39,-41,-42,-43,-44,-45,-46,-47,-102,-102,129,129,-102,-102,-102,-102,129,-57,129,129,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,-102,-54,-102,129,129,129,129,-50,-51,-52,-55,]),'LEIA':([21,23,24,25,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,80,81,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,118,119,120,121,122,123,124,125,127,129,137,139,143,145,146,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[-12,-7,-10,-11,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-102,-102,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,130,-40,130,130,-13,-20,-98,-39,-41,-42,-43,-44,-45,-46,-47,-102,-102,130,130,-102,-102,-102,-102,130,-57,130,130,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,-102,-54,-102,130,130,130,130,-50,-51,-52,-55,]),'ESCREVA':([21,23,24,25,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,80,81,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,118,119,120,121,122,123,124,125,127,129,137,139,143,145,146,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[-12,-7,-10,-11,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-102,-102,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,131,-40,131,131,-13,-20,-98,-39,-41,-42,-43,-44,-45,-46,-47,-102,-102,131,131,-102,-102,-102,-102,131,-57,131,131,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,-102,-54,-102,131,131,131,131,-50,-51,-52,-55,]),'RETORNA':([21,23,24,25,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,80,81,88,90,91,92,93,94,95,96,97,101,102,103,104,105,112,113,114,115,118,119,120,121,122,123,124,125,127,129,137,139,143,145,146,148,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,],[-12,-7,-10,-11,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-102,-102,-102,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,132,-40,132,132,-13,-20,-98,-39,-41,-42,-43,-44,-45,-46,-47,-102,-102,132,132,-102,-102,-102,-102,132,-57,132,132,-56,-58,-60,-61,-62,-63,-48,-102,-49,-102,-102,-54,-102,132,132,132,132,-50,-51,-52,-55,]),'ATE':([21,23,24,25,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,90,91,92,93,94,95,96,97,101,102,104,113,114,115,118,119,120,121,122,123,124,125,127,129,137,139,148,154,157,158,159,160,161,162,163,165,167,168,169,172,173,174,175,176,177,],[-12,-7,-10,-11,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,-40,-13,-20,-98,-39,-41,-42,-43,-44,-45,-46,-47,-102,-102,144,147,-102,-57,-56,-58,-60,-61,-62,-63,-48,-49,-102,-54,-102,144,-53,-50,-51,-52,-55,]),'SENAO':([21,23,24,25,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,90,91,92,93,94,95,96,97,101,102,104,113,114,115,118,119,120,121,122,123,124,125,143,145,146,153,154,155,156,157,158,159,160,161,162,163,165,168,169,173,174,175,176,177,],[-12,-7,-10,-11,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-18,-19,-14,-17,-9,-67,-69,-71,-73,-90,-40,-13,-20,-98,-39,-41,-42,-43,-44,-45,-46,-47,-102,-102,-102,164,-57,166,169,-56,-58,-60,-61,-62,-63,-48,-49,-54,-102,-53,-50,-51,-52,-55,]),'MULTIPLICACAO':([21,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,90,91,92,93,95,96,97,101,102,113,114,115,],[-12,-91,-59,-64,-65,-66,-68,-11,74,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-18,-19,-14,-17,-67,-69,74,-73,-90,-13,-20,-98,]),'DIVISAO':([21,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,90,91,92,93,95,96,97,101,102,113,114,115,],[-12,-91,-59,-64,-65,-66,-68,-11,75,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-18,-19,-14,-17,-67,-69,75,-73,-90,-13,-20,-98,]),'MENOR':([21,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,90,91,92,93,95,96,97,101,102,113,114,115,],[-12,-91,-59,-64,-65,65,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-18,-19,-14,-17,65,-69,-71,-73,-90,-13,-20,-98,]),'MAIOR':([21,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,90,91,92,93,95,96,97,101,102,113,114,115,],[-12,-91,-59,-64,-65,66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-18,-19,-14,-17,66,-69,-71,-73,-90,-13,-20,-98,]),'IGUAL':([21,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,90,91,92,93,95,96,97,101,102,113,114,115,],[-12,-91,-59,-64,-65,67,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-18,-19,-14,-17,67,-69,-71,-73,-90,-13,-20,-98,]),'DIFERENTE':([21,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,90,91,92,93,95,96,97,101,102,113,114,115,],[-12,-91,-59,-64,-65,68,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-18,-19,-14,-17,68,-69,-71,-73,-90,-13,-20,-98,]),'MENOR_IGUAL':([21,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,90,91,92,93,95,96,97,101,102,113,114,115,],[-12,-91,-59,-64,-65,69,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-18,-19,-14,-17,69,-69,-71,-73,-90,-13,-20,-98,]),'MAIOR_IGUAL':([21,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,90,91,92,93,95,96,97,101,102,113,114,115,],[-12,-91,-59,-64,-65,70,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-18,-19,-14,-17,70,-69,-71,-73,-90,-13,-20,-98,]),'E_LOGICO':([21,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,90,91,92,93,95,96,97,101,102,113,114,115,],[-12,-91,-59,62,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-18,-19,-14,-17,-67,-69,-71,-73,-90,-13,-20,-98,]),'OU_LOGICO':([21,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,90,91,92,93,95,96,97,101,102,113,114,115,],[-12,-91,-59,63,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-18,-19,-14,-17,-67,-69,-71,-73,-90,-13,-20,-98,]),'ENTAO':([21,27,28,29,30,31,32,33,34,36,37,40,41,45,46,47,54,58,76,77,78,79,90,91,92,93,95,96,97,101,102,113,114,115,136,138,158,],[-12,-91,-59,-64,-65,-66,-68,-11,-70,-72,-74,-92,-93,-95,-96,-97,-16,-15,-75,-91,-76,-94,-18,-19,-14,-17,-67,-69,-71,-73,-90,-13,-20,-98,143,146,143,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'lista_declaracoes':([0,],[2,]),'declaracao':([0,2,],[3,14,]),'declaracao_variaveis':([0,2,103,105,112,137,139,153,155,156,170,171,172,173,],[4,4,120,120,120,120,120,120,120,120,120,120,120,120,]),'inicializacao_variaveis':([0,2,],[5,5,]),'funcao':([0,2,],[6,6,]),'tipo':([0,2,19,20,26,82,103,105,112,137,139,153,155,156,170,171,172,173,],[7,7,52,52,52,52,126,126,126,126,126,126,126,126,126,126,126,126,]),'atribuicao':([0,2,18,22,39,55,72,103,105,112,116,127,128,137,139,141,142,144,147,148,153,155,156,167,170,171,172,173,],[8,8,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'cabecalho':([0,2,7,],[9,9,16,]),'var':([0,2,15,18,22,35,38,39,55,59,61,64,71,72,73,103,105,112,116,127,128,137,139,140,141,142,144,147,148,153,155,156,167,170,171,172,173,],[12,12,24,27,27,77,77,27,27,94,77,77,77,27,77,27,27,27,27,27,27,27,27,149,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'indice':([13,25,33,],[21,21,21,]),'lista_variaveis':([15,],[23,]),'expressao':([18,22,39,55,72,103,105,112,116,127,128,137,139,141,142,144,147,148,153,155,156,167,170,171,172,173,],[28,57,79,89,99,119,119,119,135,136,138,119,119,151,152,154,157,158,119,119,119,136,119,119,119,119,]),'expressao_logica':([18,22,39,55,72,103,105,112,116,127,128,137,139,141,142,144,147,148,153,155,156,167,170,171,172,173,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'expressao_simples':([18,22,39,55,61,72,103,105,112,116,127,128,137,139,141,142,144,147,148,153,155,156,167,170,171,172,173,],[31,31,31,31,95,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'expressao_aditiva':([18,22,39,55,61,64,72,103,105,112,116,127,128,137,139,141,142,144,147,148,153,155,156,167,170,171,172,173,],[32,32,32,32,32,96,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'expressao_multiplicativa':([18,22,39,55,61,64,71,72,103,105,112,116,127,128,137,139,141,142,144,147,148,153,155,156,167,170,171,172,173,],[34,34,34,34,34,34,97,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'operador_soma':([18,22,32,39,55,61,64,71,72,73,96,103,105,112,116,127,128,137,139,141,142,144,147,148,153,155,156,167,170,171,172,173,],[35,35,71,35,35,35,35,35,35,35,71,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'expressao_unaria':([18,22,39,55,61,64,71,72,73,103,105,112,116,127,128,137,139,141,142,144,147,148,153,155,156,167,170,171,172,173,],[36,36,36,36,36,36,36,36,101,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'fator':([18,22,35,38,39,55,61,64,71,72,73,103,105,112,116,127,128,137,139,141,142,144,147,148,153,155,156,167,170,171,172,173,],[37,37,76,78,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'operador_negacao':([18,22,39,55,61,64,71,72,73,103,105,112,116,127,128,137,139,141,142,144,147,148,153,155,156,167,170,171,172,173,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'chamada_funcao':([18,22,35,38,39,55,61,64,71,72,73,103,105,112,116,127,128,137,139,141,142,144,147,148,153,155,156,167,170,171,172,173,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'numero':([18,22,35,38,39,55,61,64,71,72,73,103,105,112,116,127,128,137,139,141,142,144,147,148,153,155,156,167,170,171,172,173,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'lista_parametros':([19,20,26,],[48,53,53,]),'parametro':([19,20,26,82,],[50,50,50,106,]),'vazio':([19,20,26,72,80,81,88,127,129,143,145,146,148,164,166,167,169,],[51,51,51,100,104,104,104,104,104,104,104,104,104,104,104,104,104,]),'operador_logico':([29,],[61,]),'operador_relacional':([31,95,],[64,64,]),'operador_multiplicacao':([34,97,],[73,73,]),'lista_argumentos':([72,],[98,]),'corpo':([80,81,88,127,129,143,145,146,148,164,166,167,169,],[103,105,112,137,139,153,155,156,137,170,171,172,173,]),'acao':([103,105,112,137,139,153,155,156,170,171,172,173,],[118,118,118,118,118,118,118,118,118,118,118,118,]),'se':([103,105,112,137,139,153,155,156,170,171,172,173,],[121,121,121,121,121,121,121,121,121,121,121,121,]),'repita':([103,105,112,137,139,153,155,156,170,171,172,173,],[122,122,122,122,122,122,122,122,122,122,122,122,]),'leia':([103,105,112,137,139,153,155,156,170,171,172,173,],[123,123,123,123,123,123,123,123,123,123,123,123,]),'escreva':([103,105,112,137,139,153,155,156,170,171,172,173,],[124,124,124,124,124,124,124,124,124,124,124,124,]),'retorna':([103,105,112,137,139,153,155,156,170,171,172,173,],[125,125,125,125,125,125,125,125,125,125,125,125,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa','parser.py',48),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','parser.py',55),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','parser.py',56),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','parser.py',64),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','parser.py',65),
  ('declaracao -> funcao','declaracao',1,'p_declaracao','parser.py',66),
  ('declaracao_variaveis -> tipo DOIS_PONTOS lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','parser.py',80),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','parser.py',87),
  ('lista_variaveis -> lista_variaveis VIRGULA var','lista_variaveis',3,'p_lista_variaveis','parser.py',92),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis','parser.py',93),
  ('var -> ID','var',1,'p_var','parser.py',102),
  ('var -> ID indice','var',2,'p_var','parser.py',103),
  ('indice -> indice ABRE_COLCHETE expressao FECHA_COLCHETE','indice',4,'p_indice','parser.py',112),
  ('indice -> ABRE_COLCHETE expressao FECHA_COLCHETE','indice',3,'p_indice','parser.py',113),
  ('indice -> ABRE_COLCHETE error','indice',2,'p_indice_error','parser.py',123),
  ('indice -> error FECHA_COLCHETE','indice',2,'p_indice_error','parser.py',124),
  ('indice -> ABRE_COLCHETE error FECHA_COLCHETE','indice',3,'p_indice_error','parser.py',125),
  ('indice -> indice ABRE_COLCHETE error','indice',3,'p_indice_error','parser.py',126),
  ('indice -> indice error FECHA_COLCHETE','indice',3,'p_indice_error','parser.py',127),
  ('indice -> indice ABRE_COLCHETE error FECHA_COLCHETE','indice',4,'p_indice_error','parser.py',128),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','parser.py',152),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo','parser.py',153),
  ('funcao -> tipo cabecalho','funcao',2,'p_funcao','parser.py',164),
  ('funcao -> cabecalho','funcao',1,'p_funcao','parser.py',165),
  ('cabecalho -> ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM','cabecalho',6,'p_cabecalho','parser.py',173),
  ('cabecalho -> <empty>','cabecalho',0,'p_cabecalho','parser.py',174),
  ('cabecalho -> ID error lista_parametros FECHA_PARENTESE corpo FIM','cabecalho',6,'p_cabecalho_error','parser.py',178),
  ('cabecalho -> ID ABRE_PARENTESE lista_parametros error corpo FIM','cabecalho',6,'p_cabecalho_error','parser.py',179),
  ('cabecalho -> ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo','cabecalho',5,'p_cabecalho_error','parser.py',180),
  ('lista_parametros -> lista_parametros VIRGULA parametro','lista_parametros',3,'p_lista_parametros','parser.py',194),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','parser.py',195),
  ('lista_parametros -> vazio','lista_parametros',1,'p_lista_parametros','parser.py',196),
  ('parametro -> tipo DOIS_PONTOS ID','parametro',3,'p_parametro','parser.py',204),
  ('parametro -> parametro ABRE_COLCHETE FECHA_COLCHETE','parametro',3,'p_parametro','parser.py',205),
  ('parametro -> tipo error ID','parametro',3,'p_parametro_error','parser.py',214),
  ('parametro -> error ID','parametro',2,'p_parametro_error','parser.py',215),
  ('parametro -> parametro error FECHA_COLCHETE','parametro',3,'p_parametro_error','parser.py',216),
  ('parametro -> parametro ABRE_COLCHETE error','parametro',3,'p_parametro_error','parser.py',217),
  ('corpo -> corpo acao','corpo',2,'p_corpo','parser.py',231),
  ('corpo -> vazio','corpo',1,'p_corpo','parser.py',232),
  ('acao -> expressao','acao',1,'p_acao','parser.py',241),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','parser.py',242),
  ('acao -> se','acao',1,'p_acao','parser.py',243),
  ('acao -> repita','acao',1,'p_acao','parser.py',244),
  ('acao -> leia','acao',1,'p_acao','parser.py',245),
  ('acao -> escreva','acao',1,'p_acao','parser.py',246),
  ('acao -> retorna','acao',1,'p_acao','parser.py',247),
  ('se -> error expressao ENTAO corpo FIM','se',5,'p_se_error','parser.py',252),
  ('se -> SE expressao error corpo FIM','se',5,'p_se_error','parser.py',253),
  ('se -> error expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se_error','parser.py',254),
  ('se -> SE expressao error corpo SENAO corpo FIM','se',7,'p_se_error','parser.py',255),
  ('se -> SE expressao ENTAO corpo error corpo FIM','se',7,'p_se_error','parser.py',256),
  ('se -> SE expressao ENTAO corpo SENAO corpo','se',6,'p_se_error','parser.py',257),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','parser.py',283),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se','parser.py',284),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','parser.py',292),
  ('repita -> error corpo ATE expressao','repita',4,'p_repita_error','parser.py',296),
  ('repita -> REPITA corpo error expressao','repita',4,'p_repita_error','parser.py',297),
  ('atribuicao -> var ATRIBUICAO expressao','atribuicao',3,'p_atribuicao','parser.py',306),
  ('leia -> LEIA ABRE_PARENTESE var FECHA_PARENTESE','leia',4,'p_leia','parser.py',311),
  ('leia -> LEIA ABRE_PARENTESE error FECHA_PARENTESE','leia',4,'p_leia_error','parser.py',316),
  ('escreva -> ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESE','escreva',4,'p_escreva','parser.py',322),
  ('retorna -> RETORNA ABRE_PARENTESE expressao FECHA_PARENTESE','retorna',4,'p_retorna','parser.py',329),
  ('expressao -> expressao_logica','expressao',1,'p_expressao','parser.py',336),
  ('expressao -> atribuicao','expressao',1,'p_expressao','parser.py',337),
  ('expressao_logica -> expressao_simples','expressao_logica',1,'p_expressao_logica','parser.py',343),
  ('expressao_logica -> expressao_logica operador_logico expressao_simples','expressao_logica',3,'p_expressao_logica','parser.py',344),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','parser.py',352),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','parser.py',353),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','parser.py',361),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_expressao_aditiva','parser.py',362),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','parser.py',370),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','parser.py',371),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','parser.py',379),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria','parser.py',380),
  ('expressao_unaria -> operador_negacao fator','expressao_unaria',2,'p_expressao_unaria','parser.py',381),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','parser.py',390),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operador_relacional','parser.py',391),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacional','parser.py',392),
  ('operador_relacional -> DIFERENTE','operador_relacional',1,'p_operador_relacional','parser.py',393),
  ('operador_relacional -> MENOR_IGUAL','operador_relacional',1,'p_operador_relacional','parser.py',394),
  ('operador_relacional -> MAIOR_IGUAL','operador_relacional',1,'p_operador_relacional','parser.py',395),
  ('operador_soma -> MAIS','operador_soma',1,'p_operador_soma','parser.py',416),
  ('operador_soma -> MENOS','operador_soma',1,'p_operador_soma','parser.py',417),
  ('operador_logico -> E_LOGICO','operador_logico',1,'p_operador_logico','parser.py',425),
  ('operador_logico -> OU_LOGICO','operador_logico',1,'p_operador_logico','parser.py',426),
  ('operador_negacao -> NEGACAO','operador_negacao',1,'p_operador_negacao','parser.py',432),
  ('operador_multiplicacao -> MULTIPLICACAO','operador_multiplicacao',1,'p_operador_multiplicacao','parser.py',437),
  ('operador_multiplicacao -> DIVISAO','operador_multiplicacao',1,'p_operador_multiplicacao','parser.py',438),
  ('fator -> ABRE_PARENTESE expressao FECHA_PARENTESE','fator',3,'p_fator','parser.py',443),
  ('fator -> var','fator',1,'p_fator','parser.py',444),
  ('fator -> chamada_funcao','fator',1,'p_fator','parser.py',445),
  ('fator -> numero','fator',1,'p_fator','parser.py',446),
  ('fator -> ABRE_PARENTESE expressao','fator',2,'p_fator_error','parser.py',454),
  ('numero -> NUM_INTEIRO','numero',1,'p_numero','parser.py',459),
  ('numero -> NUM_PONTO_FLUTUANTE','numero',1,'p_numero','parser.py',460),
  ('numero -> NUM_NOTACAO_CIENTIFICA','numero',1,'p_numero','parser.py',461),
  ('chamada_funcao -> ID ABRE_PARENTESE lista_argumentos FECHA_PARENTESE','chamada_funcao',4,'p_chamada_funcao','parser.py',471),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','parser.py',476),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','parser.py',477),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_lista_argumentos','parser.py',478),
  ('vazio -> <empty>','vazio',0,'p_vazio','parser.py',486),
]
