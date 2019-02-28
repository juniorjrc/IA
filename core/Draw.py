import random

class Draw:
    pass

    @staticmethod # Desenha o Mapa neutro, mapa pura grama
    def drawNeutralMap(self, size):
        m = []
        for i in range(size[0]):
            m.append([])
            for j in range(size[1]):
                m[i].append(1)
                
        return m

    @staticmethod # desenha os detalhes no mapa de acordo com os parametros
    def drawDetails(m, details, element):
        for key in details.keys():
            while(details[key] > 0):
                line = random.randint(0, len(m)-1)
                column = random.randint(0, len(m[line])-1)
                
                if(m[line][column] == element['grama']):
                    m[line][column] = element[key]
                    details[key] -= 1
        return m

    @staticmethod # desenha uma matriz do mapa
    def drawMatrix(m):
        for i in range(len(m)):
            print(m[i])

    @staticmethod # desenha o player no mapa
    def drawPlayer(m, element):
        while(True):
            line = random.randint(0, len(m)-1)
            column = random.randint(0, len(m[line])-1)

            if(m[line][column] == element['grama']):
                m[line][column] = element['player']
                break
            
        return m

    @staticmethod # desenha o destino no mapa
    def drawDestiny(m, element):
        while(True):
            line = random.randint(0, len(m)-1)
            column = random.randint(0, len(m[line])-1)

            if(m[line][column] == element['grama']):
                m[line][column] = element['destino']
                break
            
        return m        
                    

            
