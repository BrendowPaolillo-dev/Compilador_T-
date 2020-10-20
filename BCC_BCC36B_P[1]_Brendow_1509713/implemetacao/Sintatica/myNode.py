from anytree.exporter import DotExporter
from anytree import Node, RenderTree

p = [0,0,0,0]

root = None
id = 0
        

class MyNode(Node):
    def __init__(self, typeN, parent = None, children=None):
        super(Node, self).__init__()
        global id
        self.name = typeN
        self.id = id
        id += 1
        # self.value = value 
        self.parent = parent
        
        if children:
            self.children = children
            
    def __str__(self):  
        return (str(self.id) + ' ' + self.name + ' ' + str(self.parent) + ' ' + str(self.children))


def p_programa(p):
    "programa : lista_declaracoes"
    global root
    father = MyNode('Programa')
    root = father
    p[0] = father
    p[2] = MyNode("teste")
    p[3] = MyNode("teste2")
    p[1] = MyNode("lista_declaracoes", father, [p[2], p[3]])
    
p_programa(p)
print(p)


# DotExporter(p[0]).to_picture("arvore_sintatica.png")