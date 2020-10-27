# Relatório Sintática

## Introdução

Para a verificação da gramática a ser utilizada pela linguagem T++ foi-se implementado o analisador sintático, no qual verifica a ordem (estrutura) dos tokens disponíveis, resultando uma Árvore Sintática Abstrata (ASA) e verificando erros de implementação do arquivo .tpp

### Descrição BNF

A gramática BNF foi disponibilizada pelo professor que ministra a disciplina, Rogério A. Gonçalves, e pode ser visualizada em: 

[ebnf-tpp-symbols.odt](https://docs.google.com/document/d/1oYX-5ipzL_izj_hO8s7axuo2OyA279YEhnAItgXzXAQ/edit?usp=drivesdk)

À esquerda da lista temos a regra e a esquerda os nós terminais ou não terminais que são gerado e necessários para se compreender as regras gramaticais da linguagem. 

## Yacc Ply

A implementação da gramática utilizou uma biblioteca disponibilizada no gerenciador de pacotes do Python (pip), no qual simplifica o reconhecimento das regras léxicas e sintáticas, por estabelecer uma classe de objetos que possui funções prontas para a implementação do compilador.

A regras gramaticais são definidas por uma string organizadas como no arquivo sobre as regras da BNF.

A biblioteca então divide cada token e ID reconhecido como um elemento do vetor, iniciando no índice 0.

![Relato%CC%81rio%20Sinta%CC%81tica/Untitled.png](Relato%CC%81rio%20Sinta%CC%81tica/Untitled.png)

## Implementação

Para a implementação da ASA foi criada uma classe no qual gera o nó de cada token reconhecido.

### Classe de nó

Derivada da classe Node da biblioteca AnyTree, herdando assim o nome do nó e o pai (parent) da classe. Para facilitar a implementação do código, foi adicionado um parâmetro a mais, o children (filho), e um campo de id caso seja necessário durante o desenvolvimento do compilador.

![Relato%CC%81rio%20Sinta%CC%81tica/Untitled%201.png](Relato%CC%81rio%20Sinta%CC%81tica/Untitled%201.png)

### Relacionando os filhos

Após definir o nó e adicionar as strings da BNF, é necessário relacionar os nós conforme são reconhecidos pelo analisador sintático e atribuir os valores nos nós folhas.

Para compreender melhor, veja o exemplo da regra abaixo:

![Relato%CC%81rio%20Sinta%CC%81tica/Untitled%202.png](Relato%CC%81rio%20Sinta%CC%81tica/Untitled%202.png)

A estrutura da árvore deve ser como descrito nos comentários entre as linhas 72 e 77. Porém o DOIS_PONTOS gerado, é um símbolo terminal, assim então é necessário criar um valor com o Token DOIS_PONTOS e adicionar um nó folha a ele com o caractere que representa os dois pontos (":").

Já o nó pai de todos (declaracao_variaveis) deve ser relacionado aos seus filhos.

### Saída

A biblioteca do AnyTree, possui funções de exportação da árvore para um arquivo de imagem ou um Dotfile. O arquivos finais se chamam tree.png e tree.dot.

A ASA resultante após a execução do código de teste "teste-1.tpp" é a seguinte:

![Relatório Sintática/uniquetree.png](Relato%CC%81rio%20Sinta%CC%81tica/uniquetree.png)

## Execução

Para a execução do analisador sintático, acesse a pasta /implementacao/Sintatica e execute o arquivo [parser.py](http://parser.py) da seguinte forma:

```python
python3 parser.py ./sintatica-testes/nomedoarquivodeteste.tpp
```
