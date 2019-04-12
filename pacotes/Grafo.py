class Grafo:
    def __init__(self):
        self.nos    = nos()
        self.grafo  = grafo()

#Utilizado da versão do Bruno com alguns ajustes para geração do grafo e reconhecimento dos vizinhos
def grafo(matriz):
    nos             = []  # nos do grafo
    vizinhos        = []  # vizinhos dos nos
    cont            = 0  # contador
    nodes           = []
    c               = 1

    for linha in range(len(matriz)):
        nodes.append([])
        for coluna in range(len(matriz[linha])):
            nodes[linha].append([coluna])
            nodes[linha][coluna] = c
            c += 1


    for linha in range(len(nodes)):
        for coluna in range(len(nodes[linha])):
            nos.append(nodes[linha][coluna])
            vizinhos.append([])

            if (linha < (len(matriz) - 2)):  # vizinho abaixo?
                vizinhos[cont].append(nodes[linha + 1][coluna])

            if (coluna < (len(matriz[linha]) - 1)):  # vizinho a direita?
                vizinhos[cont].append(nodes[linha][coluna + 1])

            if (coluna > 0):  # vizinho a esquerda?
                vizinhos[cont].append(nodes[linha][coluna - 1])

            if (linha != 0):  # vizinho acima?
                vizinhos[cont].append(nodes[linha - 1][coluna])

            cont += 1
    grafo = vizinhos

    return grafo

def nos(m1, m2):
    nos = []
    for i in range(m1 * m2):
        nos.append(i+1)
    return nos
