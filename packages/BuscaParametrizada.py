class No(object):
    def __init__(self, pai=None, valor1=None, valor2=None, valor3=None, anterior=None, proximo=None):
        self.pai       = pai
        self.valor1    = valor1
        self.valor2    = valor2
        self.valor3    = valor3
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, v1, v2, v3, p):
        novo_no = No(p, v1, v2, v3, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, v1, v2, v3, p):

        novo_no = No(p, v1, v2, v3, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no
    
    # INSERE NO FIM DA LISTA
    def inserePos_X(self, v1, v2, v3, p):
        
        if self.head is None:
            self.inserePrimeiro(v1,v2,v3,p)
        else:
            atual = self.head
            while atual.valor2 < v2:
                atual = atual.proximo
                if atual is None: break
            
            if atual == self.head:
                self.inserePrimeiro(v1,v2,v3,p)
            else:
                if atual is None:
                    self.insereUltimo(v1,v2,v3,p)
                else:
                    novo_no = No(p,v1,v2,v3,None,None)
                    
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual


    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            str.append(aux.valor1)
            aux = aux.proximo
        
        return str
    
    def exibeArvore(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        return caminho
    
    def exibeArvore1(self,valor):
        
        
        atual = self.head
        while atual.valor1 != valor:
            atual = atual.proximo
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        return caminho
    
    
    def exibeArvore2(self, v1, v2):
        
        atual = self.tail
        
        while atual.valor1 != v1 or atual.valor2 != v2:
            atual = atual.anterior
        
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        return caminho
    
    
    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail



class busca(object):
    
    def custo_uniforme(self, inicio, fim, nos, grafo):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()
            if atual.valor1 == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.valor1,atual.valor2)
                return caminho, atual.valor2
        
            ind = nos.index(atual.valor1)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]
                valor = atual.valor2 + grafo[ind][i][1]
                flag = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=valor:
                            flag = False
                        break
                
                if flag:
                    l1.inserePos_X(novo, valor , valor, atual)
                    l2.inserePos_X(novo, valor, valor, atual)
                    linha = []
                    linha.append(novo)
                    linha.append(valor)
                    visitado.append(linha)
                    
        return "Caminho não encontrado"


########################################
#  ENCONTA POSIÇÃO DO ROBO E DESTINO   #
########################################
def achaPosicao(caminho, m1, m2):
    contador        = 0
    line            = []
    column          = []
    if caminho == None:
        print("Não existe o melhor caminho de acordo com o limite solicitado!!")
    else:
        for p, x in enumerate(caminho):
            for y in range(m1):
                for z in range(m2):
                    contador += 1
                    if contador == x:
                        line.append(y)
                        column.append(z)

            contador = 0

    return line, column

#EXECUÇÃO DO ALGORITMO
def exec(nos, grafo, m1, m2 , grafoPesos, jogador, destino):

    sol = busca()
    caminho = []
    caminho, custo = sol.custo_uniforme(jogador, destino, nos, grafoPesos)
    print("Custo Uniforme: ",caminho[::-1],"\tcusto do caminho: ",custo)
    caminho.reverse()
    proxLines = achaPosicao(caminho, m1, m2)[0]
    proxColumns = achaPosicao(caminho, m1, m2)[1]
    return proxLines, proxColumns
