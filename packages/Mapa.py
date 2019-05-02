from packages.Retangulo import *
class Mapa:
    def __init__(self, nome, linha, coluna):
        self.nome 			= nome
        self.linha 		    = linha
        self.coluna 		= coluna
        self.retangulo  	= makeRetangulos(linha, coluna) #Objeto responsável pelos retangulos do mapa

def makeMapa(nome, linha, coluna):
    mapa = Mapa(nome, linha, coluna)
    return mapa

#CRIA OS RETANGULOS COM SEUS RESPECTIVOS ATRIBUTOS
def makeRetangulos(linhas, colunas):
    retangulos      = [[Retangulo(0, None, x, y, "gray", None) for x in range(linhas)] for y in range(colunas)]
    setaPosicoesRetangulo(retangulos, linhas, colunas)

    return retangulos

#SETA AS POSIÇÕES NOS RETANGULOS
def setaPosicoesRetangulo(retangulos, linhas, colunas):
    posicao = 1
    for x in range(linhas):
        for y in range(colunas):
            retangulos[x][y].posicao = posicao
            posicao += 1


    