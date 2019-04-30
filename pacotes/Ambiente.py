from pacotes import Elementos as e
valorElemento = e.Elementos()
#Implantado na v1.2, recebe o ambiente de iteração entre ambiente, robo e destino
class Ambiente:

    def __init__(self, matriz):
        self.ambiente = matriz

    #Aqui ficarão todos os códigos de busca
    def geraMatrizPesos(self, matriz):
        matrizPesos = matriz
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                matrizPesos[linha][coluna] = valorElemento.pesos[0][matriz[linha][coluna]]
        
        return matrizPesos