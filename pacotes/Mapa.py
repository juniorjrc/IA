class Mapa:
    def __init__(self, nome, altura, largura):
        self.nome 			= nome
        self.altura 		= altura
        self.largura 		= largura
        self.retangulo  	= makeRetangulos(altura, largura) #Objeto responsável pelos retangulos do mapa

    class Retangulo:
        def __init__(self, x, y, tipo, cor, estaOcupado, inimigo):
            self.x 				= x
            self.y 				= y
            self.tipo 			= tipo
            self.cor 			= cor
            self.estaOcupado 	= estaOcupado
            self.inimigo 		= inimigo

#Gera o mapa chamando a classe Mapa, que por padrão possui o objeto Retangulo, que compõe os retangulos no mapa
def makeMapa(nome, altura, largura):
    retangulo = Mapa(nome, altura, largura)
    return retangulo

#Gera os retangulos do mapa
def makeRetangulos(altura, largura):
    retangulos = [[Mapa.Retangulo(x, y, "Surface", "black", False, "None") for x in range(altura)] for y in range(largura)]
    return retangulos