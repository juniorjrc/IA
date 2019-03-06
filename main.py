#=======================================================#
#PROJETO IA 2019                                        #
#LEIA OS COMENTÁRIOS DO CÓDIGO PARA MAIOR COMPREENSÃO   #
#=======================================================#

from pacotes.Mapa import *

#Executor do programa
root = tk.Tk()
root.title("Mapa")
frame = tk.Frame()
frame.pack()

#Define o tamanho da matriz (No caso uma matriz 10 por 10)
m1 = 20
m2 = 20

#===========================================================#
# Mapa ideal para o problema do robo                        #
# matriz 20x20                                              #
# montanha, colina, floresta, gelo, mar, agua, areia, solo  #
# 55, 35, 45, 25, 60, 40, 100, 40                           #
#===========================================================#

#Largura x altura do mapa
largura, altura = 800, 600

#Gera o mapa e APENAS O MAPA em formato matriz
mapa        = makeMapa("test", m1, m2)
matriz      = [[0 for x in range(m1)] for y in range(m2)]

#Preenche o mapa com as cores neutras
preencheMapa(mapa, matriz, m1, m2)

#Utiliza a biblioteca do canvas para desenho da matriz em tela.
desenhaMapa(largura, altura, matriz, m1, m2)

root.mainloop()