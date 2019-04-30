class Grafo:
    def __init__(self, matriz, m1 , m2):
        self.nos    = nos(m1, m2)
        self.grafo  = grafo(matriz)

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

def grafoPesos(matriz, matrizPesos):
    vizinhos        = []  # vizinhos dos nos
    cont            = 0  # contador
    nodes           = []
    c               = 1
    vNo = []
    vAresta = []
    g = []

    for linha in range(len(matriz)):
        nodes.append([])
        for coluna in range(len(matriz[linha])):
            nodes[linha].append([coluna])
            nodes[linha][coluna] = c
            c += 1
    c = 0
    qc = 0
    for linha in range(len(nodes)):
        for coluna in range(len(nodes[linha])):
            vizinhos.append([])
            if (linha < (len(matriz) - 2)):  # vizinho abaixo?
                vizinhos[cont].append(nodes[linha + 1][coluna])
                vizinhos[cont].append(matrizPesos[linha + 1][coluna])
                vNo.append(nodes[linha + 1][coluna])
                vAresta.append(matrizPesos[linha + 1][coluna])
                qc += 1


            if (coluna < (len(matriz[linha]) - 1)):  # vizinho a direita?
                vizinhos[cont].append(nodes[linha][coluna + 1])
                vizinhos[cont].append(matrizPesos[linha][coluna + 1])
                vNo.append(nodes[linha][coluna + 1])
                vAresta.append(matrizPesos[linha][coluna + 1])
                qc += 1

            if (coluna > 0):  # vizinho a esquerda?
                vizinhos[cont].append(nodes[linha][coluna - 1])
                vizinhos[cont].append(matrizPesos[linha][coluna - 1])
                vNo.append(nodes[linha][coluna - 1])
                vAresta.append(matrizPesos[linha][coluna - 1])
                qc += 1

            if (linha != 0):  # vizinho acima?
                vizinhos[cont].append(nodes[linha - 1][coluna])
                vizinhos[cont].append(matrizPesos[linha - 1][coluna])
                vNo.append(nodes[linha - 1][coluna])
                vAresta.append(matrizPesos[linha - 1][coluna])
                qc += 1
            aux1 = []
            b = 0
            for v in range (qc):
                aux2 = []
                aux2.append(vNo[v])
                aux2.append(vAresta[v])
                aux1.append(aux2)
                b += 1
                if b == qc:
                    vNo.clear()
                    vAresta.clear()
                    break
        
            
            cont += 1
            qc = 0
            g.append(aux1)
    return g

def nos(m1, m2):
    nos = []
    for i in range(m1 * m2):
        nos.append(i+1)
    return nos
