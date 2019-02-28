#-------------
#IMPORTS
from core.Draw import Draw
from core.Elements import Elements



class Map:
    pass

    #Inicializa o Mapa
    def __init__(self, size):
        self.map = Draw.drawNeutralMap(0,size)

    #Desenha os detalhes no mapa
    def drawDetails(self, details):
        self.map = Draw.drawDetails(self.map, details, Elements.getElements(0))

    #Desenha o mapa em Matriz
    def drawMap(self):
        Draw.drawMatrix(self.map)
        
    #Desenha o Player
    def drawPlayer(self):
        self.map = Draw.drawPlayer(self.map, Elements.getElements(0))
        
    #Desenha o destino
    def drawDestiny(self):
        self.map = Draw.drawDestiny(self.map, Elements.getElements(0))

    #retorna o mapa
    def getMap(self):
        return self.map
    

        



    
    
