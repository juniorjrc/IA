from src.Node import Node

class Lista:

    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def add(self,valor, pai):
        no = Node(valor, None, None, pai)

        if self.inicio is None:
            self.inicio = no
            self.fim = no
        else:
            no.anterior = self.fim
            self.fim.proximo = no
            self.fim = no

    def removeFirst(self):
        if self.inicio is None:
            return None
        no = self.inicio
        self.inicio = self.inicio.proximo
        if self.inicio is not None:
            self.inicio.anterior = None
        else:
            self.fim = None
        return no

    
    def removePosicao(self, valor):
        cont = 0
        no = self.inicio
        while no is not None:
            if cont == valor:
                if no.anterior is None:
                    self.inicio = self.inicio.proximo
                    
                else:
                    no.anterior.proximo = no.proximo
                    no.proximo.anterior = no.anterior
                break
            else :
                no = no.proximo
                cont = cont + 1

    def showTree(self):
        atual = self.fim
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.valor['identificador'])
            atual = atual.pai
        caminho.append(atual.valor['identificador'])
        return caminho
    
    def show(self):
        no  = self.inicio
        print("[none] <-->", end="")
        while no is not None:
            print(" {0} <--> ". format(no.valor), end="")
            no = no.proximo
        print("[none]")

    def isEmpty(self):
        if self.inicio is None:
            return True
        return False


## Implementação
#l = Lista()
#l.add(10,None)
#l.add(30,10)
#l.add(1, 10)
#l.show()
#l.removePosicao(1)
#l.show()

