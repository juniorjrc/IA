class Conversor:

    @staticmethod
    def toGrafo(matriz):
        nos = [] # nos do grafo
        vizinhos = [] # vizinhos dos nos
        cont = 0 # contador
        
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                nos.append(matriz[linha][coluna])
                nos[cont]['identificador'] = cont
                vizinhos.append([])
                
                if(linha != 0): #  vizinho acima?
                    vizinhos[cont].append(matriz[linha - 1][coluna])
                    
                if(linha < (len(matriz) - 2)):# vizinho abaixo?
                    vizinhos[cont].append(matriz[linha + 1][coluna])
                    
                if(coluna > 0):# vizinho a esquerda?
                    vizinhos[cont].append(matriz[linha][coluna - 1])
                    
                if(coluna < (len(matriz[linha]) - 1)):# vizinho a direita?
                    vizinhos[cont].append(matriz[linha][coluna + 1])

                cont += 1

        return nos, vizinhos
