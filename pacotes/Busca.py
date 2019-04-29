import pacotes.Grafo as g
from pacotes.Jogador import *
from pacotes.Destino import *

class No(object):
    def __init__(self, pai=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai            = pai
        self.valor1         = valor1
        self.valor2         = valor2
        self.anterior       = anterior
        self.proximo        = proximo


class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, v1, v2, p):
        novo_no = No(p, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, v1, v2, p):

        novo_no = No(p, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
        self.tail = novo_no

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
    
    
    def primeiro(self):
        return self.head


class busca(object):

    def bidirecional(self, inicio, fim, nos, grafo):
        
        l1 = lista()
        l2 = lista()
        l3 = lista()
        l4 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)
        linha = []
        linha.append(inicio)
        linha.append(1)
        visitado.append(linha)
        
        l3.insereUltimo(fim,0,None)
        l4.insereUltimo(fim,0,None)
        linha = []
        linha.append(fim)
        linha.append(2)
        visitado.append(linha)
        
        while True:
            flag1 = True
            while flag1:
                atual = l1.deletaPrimeiro()
                ind = nos.index(atual.valor1)
                for i in range(len(grafo[ind])):
                    novo = grafo[ind][i]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1] == 1:
                                flag2 = False
                            else:
                                flag3 = True
                            break
                    # for j
                        
                    if flag2:
                        l1.insereUltimo(novo, atual.valor2 + 1 , atual)
                        l2.insereUltimo(novo, atual.valor2 + 1, atual)
                        
                        if flag3:
                            caminho = []
                            caminho = l2.exibeArvore()
                            caminho = caminho[::-1]
                            caminho += l4.exibeArvore1(novo)
                            return caminho
                        else:
                            linha = []
                            linha.append(novo)
                            linha.append(1)
                            visitado.append(linha)
                        # if flag3
                    # if flag2
                # for i
                        
                if(l1.vazio()!=True):
                    aux = l1.primeiro()
                    #print("Primeiro: ",aux.valor1,aux.valor2)
                    #print("Atual: ",atual.valor1,atual.valor2)
                    if(atual.valor2 == aux.valor2):
                        flag1 = True
                    else:
                        flag1 = False
                
            flag1 = True
            while flag1:
                atual = l3.deletaPrimeiro()
                ind = nos.index(atual.valor1)
                for i in range(len(grafo[ind])):
                    novo = grafo[ind][i]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1] == 2:
                                flag2 = False
                            else:
                                flag3 = True
                            break
                        
                    if flag2:
                        l3.insereUltimo(novo, atual.valor2 + 1 , atual)
                        l4.insereUltimo(novo, atual.valor2 + 1, atual)
                        
                        if flag3:
                            caminho = []
                            caminho = l4.exibeArvore()
                            caminho = caminho[::-1]
                            caminho += l2.exibeArvore1(novo)
                            return caminho
                        else:
                            linha = []
                            linha.append(novo)
                            linha.append(2)
                            visitado.append(linha)
                        
                if(l3.vazio() != True):
                    aux = l3.primeiro()
                    if(atual.valor2 == aux.valor2):
                        flag1 = True
                    else:
                        flag1 = False

    def amplitude(self, inicio, fim, nos, grafo):

        l1          = lista()
        l2          = lista()
        visitado    = []

        l1.insereUltimo(inicio, 0, None)
        l2.insereUltimo(inicio, 0, None)
        visitado.append(inicio)
        achou = False

        while l1.vazio() is not None and not achou:
            atual = l1.deletaPrimeiro()
            ind = nos.index(atual.valor1)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i]
                flag = True
                for j in range(len(visitado)):
                    if visitado[j] == novo:
                        flag = False
                        break

                if flag:
                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)
                    visitado.append(novo)
                    if novo == fim:
                        caminho = []
                        caminho = l2.exibeArvore()
                        return caminho

    def profundidade(self, inicio, fim, nos, grafo):

        l1          = lista()
        l2          = lista()
        visitado    = []

        l1.insereUltimo(inicio, 0, None)
        l2.insereUltimo(inicio, 0, None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        achou = False

        while l1.vazio() == False and not achou:
            atual = l1.deletaUltimo()
            ind = nos.index(atual.valor1)
            for i in range(len(grafo[ind]) - 1, -1, -1):
                novo = grafo[ind][i]
                visit = False
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= atual.valor2:
                            visit = True
                if visit == False:
                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2 + 1)
                    visitado.append(linha)
                    if novo == fim:
                        caminho = []
                        caminho = l2.exibeArvore()
                        return caminho

    def profundidadeLimitada(self, inicio, fim, limite, nos, grafo):

        l1          = lista()
        l2          = lista()
        visitado    = []

        l1.insereUltimo(inicio, 0, None)
        l2.insereUltimo(inicio, 0, None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        achou = False

        while l1.vazio()==False and not achou:
            atual = l1.deletaUltimo()
            ind = nos.index(atual.valor1)

            if atual.valor2 < limite:
                for i in range(len(grafo[ind]) - 1, -1, -1):
                    novo = grafo[ind][i]
                    visit = False
                    for j in range(len(visitado)):
                        if visitado[j][0] == novo:
                            if visitado[j][1] <= atual.valor2:
                                visit = True
                    if visit == False:
                        l1.insereUltimo(novo, atual.valor2 + 1, atual)
                        l2.insereUltimo(novo, atual.valor2 + 1, atual)
                        linha = []
                        linha.append(novo)
                        linha.append(atual.valor2 + 1)
                        visitado.append(linha)
                        if novo == fim:
                            caminho = []
                            caminho = l2.exibeArvore()
                            return caminho

    def aprofundamentoInterativo(self, inicio, fim, nos, grafo):
        l1          = lista()
        l2          = lista()
        visitado    = []

        for limite in range(25):
            l1.insereUltimo(inicio, 0, None)
            l2.insereUltimo(inicio, 0, None)
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
            achou = False

            while l1.vazio()==False and not achou:
                atual = l1.deletaUltimo()
                ind = nos.index(atual.valor1)

                if atual.valor2 < limite:
                    for i in range(len(grafo[ind]) - 1, -1, -1):
                        novo = grafo[ind][i]
                        visit = False
                        for j in range(len(visitado)):
                            if visitado[j][0] == novo:
                                if visitado[j][1] <= atual.valor2:
                                    visit = True
                        if visit == False:
                            l1.insereUltimo(novo, atual.valor2 + 1, atual)
                            l2.insereUltimo(novo, atual.valor2 + 1, atual)
                            linha = []
                            linha.append(novo)
                            linha.append(atual.valor2 + 1)
                            visitado.append(linha)
                            if novo == fim:
                                caminho = []
                                caminho = l2.exibeArvore()
                                return caminho


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

#Método de execução dos algoritmos
def exec(nos, grafo, m1, m2):
    algoritmo   = int(input("Escolha o Algoritmo:\n1 - Amplitude\n2 - Profundidade\n3 - Profundidade Limitada\n4 - Aprofundamento Interativo\n5 - Bidirecional\nOPÇÃO: "))
    L           = busca()

    caminho     = []
    j           = Jogador(m1, m2)
    d           = Destino(m1, m2)

    if algoritmo == 1:
        #AMPLITUDE
        ####################################
        caminho = L.amplitude(j.posicaoJogador, d.posicaoDestino, nos, grafo)
        caminho.reverse()
        print("Amplitude: ", caminho)
        ####################################

    if algoritmo == 2:
        #PROFUNDIDADE
        ####################################
        caminho = L.profundidade(j.posicaoJogador, d.posicaoDestino, nos, grafo)
        caminho.reverse()
        print("Profundidade: ", caminho)
        ####################################

    if algoritmo == 3:
        #PROFUNDIDADE LIMITADA
        ####################################
        lim = int(input("Insira o limite : "))
        caminho = L.profundidadeLimitada(j.posicaoJogador, d.posicaoDestino, lim, nos, grafo)
        if caminho != None:
            caminho.reverse()
        print("Profunidade Limitada: ", caminho)
        ####################################

    if algoritmo == 4:
        #APROFUNDAMENTO INTERATIVO
        ####################################
        caminho = L.aprofundamentoInterativo(j.posicaoJogador, d.posicaoDestino, nos, grafo)
        caminho.reverse()
        print("Aprofundamento iterativo: ", caminho)
        ####################################
    
    if algoritmo == 5:
        #BIDIRECIONAL
        ####################################
        caminho = L.bidirecional(j.posicaoJogador, d.posicaoDestino, nos, grafo)
        caminho.reverse()
        print("Bidirecional: ",caminho)
        ####################################

    proxLines = achaPosicao(caminho, m1, m2)[0]
    proxColumns = achaPosicao(caminho, m1, m2)[1]

    return proxLines, proxColumns




