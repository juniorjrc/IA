from Node import Node

class Lista:

    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def add(self,valor):
        no = Node(valor, None, None)

        if self.inicio is None:
            self.inicio = no
            self.fim = no
        else:
            no.anterior = self.fim
            self.fim.proximo = no
            self.fim = no

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
                
    def show(self):
        no  = self.inicio
        print("[none] <-->", end="")
        while no is not None:
            print(" {0} <--> ". format(no.valor), end="")
            no = no.proximo
        print("[none]")



## Implementação
l = Lista()
l.add(10)
l.add(30)
l.add(1)
l.show()
l.removePosicao(1)
l.show()

