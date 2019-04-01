from src.Elementos import *
import random 
class Desenhista:

    @staticmethod
    def inserirElementos(matriz, L, C, elementos):
        for e in elementos:
        #para cada elemento
            nome = '{0}'.format(e) #captura o nome do elemento
            qtd = 0 #quantia atual
            x = 0  #posicao atual
            y = 0  #posicao atual
            while(qtd < elementos[nome]):
            #enquanto a quantia for menor que aquela definida no Mapa.py

                ocupado = True
                while(ocupado):
                    x = random.randint(0, L-1)#random X
                    y = random.randint(0, C-1)#random Y
                    
                    if matriz[x][y]['nome'] is 'solo':
                    #se a posicao é solo então pode trocar
                        ocupado = False
                        qtd += 1
                
                matriz[x][y] = Elementos.get()[nome]
                #a matriz troca o valor
                
        return matriz
        #retorna a matriz com elementso preenchidos
    
    def inserirJogadoreDestino(matriz, L, C, jogador, destino):
        matriz[jogador[0]][jogador[1]] = Elementos.get()['jogador']
        matriz[destino[0]][destino[1]] = Elementos.get()['destino']

        return matriz
        
            
