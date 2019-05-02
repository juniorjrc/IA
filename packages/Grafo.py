class Grafo():
    def __init__(self, matriz):
        self.nos, self.nosPosicionados = self.pegaNos(matriz)
        self.grafo, self.grafoParametrizado = self.geraGrafo(matriz, self.nosPosicionados)
    
    def pegaNos(self, matriz):
        nos = []
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                nos.append(matriz[linha][coluna].posicao)
        
        nosPosicionados = []

        for linha in range(len(matriz)):
            nosPosicionados.append([])
            for coluna in range(len(matriz[linha])):
                nosPosicionados[linha].append(matriz[linha][coluna].posicao)
        
        return nos, nosPosicionados

    def geraGrafo(self, matriz, nosPosicionados):
        vizinhos        = []  # vizinhos dos nos
        posicaoPeso     = []
        cont            = 0  # contador
        grafoPesos      = []
        vNo             = []
        vAresta         = []
        qc = 0

        for linha in range(len(nosPosicionados)):
            for coluna in range(len(nosPosicionados[linha])):
                vizinhos.append([])
                posicaoPeso.append([])

                if (linha < (len(matriz) - 2)):  # vizinho abaixo?
                    vizinhos[cont].append(matriz[linha + 1][coluna].posicao)
                    posicaoPeso[cont].append(matriz[linha + 1][coluna].posicao)
                    posicaoPeso[cont].append(matriz[linha + 1][coluna].pesos)
                    vNo.append(matriz[linha + 1][coluna].posicao)
                    vAresta.append(matriz[linha + 1][coluna].pesos)
                    qc += 1

                if (coluna < (len(matriz[linha]) - 1)):  # vizinho a direita?
                    vizinhos[cont].append(matriz[linha][coluna + 1].posicao)
                    posicaoPeso[cont].append(matriz[linha][coluna + 1].posicao)
                    posicaoPeso[cont].append(matriz[linha][coluna + 1].pesos)
                    vNo.append(matriz[linha][coluna + 1].posicao)
                    vAresta.append(matriz[linha][coluna + 1].pesos)
                    qc += 1

                if (coluna > 0):  # vizinho a esquerda?
                    vizinhos[cont].append(matriz[linha][coluna - 1].posicao)
                    posicaoPeso[cont].append(matriz[linha][coluna - 1].posicao)
                    posicaoPeso[cont].append(matriz[linha][coluna - 1].pesos)
                    vNo.append(matriz[linha][coluna - 1].posicao)
                    vAresta.append(matriz[linha][coluna - 1].pesos)
                    qc += 1

                if (linha != 0):  # vizinho acima?
                    vizinhos[cont].append(matriz[linha - 1][coluna].posicao)
                    posicaoPeso[cont].append(matriz[linha - 1][coluna].posicao)
                    posicaoPeso[cont].append(matriz[linha - 1][coluna].pesos)
                    vNo.append(matriz[linha - 1][coluna].posicao)
                    vAresta.append(matriz[linha - 1][coluna].pesos)
                    qc += 1
                
                aux1 = []
                c = 0
                for value in range (qc):
                    aux2 = []
                    aux2.append(vNo[value])
                    aux2.append(vAresta[value])
                    aux1.append(aux2)
                    c += 1
                    if c == qc:
                        vNo.clear()
                        vAresta.clear()
                        break

                cont += 1
                qc = 0
                grafoPesos.append(aux1)
        grafo = vizinhos
        return grafo, grafoPesos

