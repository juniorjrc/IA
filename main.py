from src.Mapa import *
from src.Conversor import *
from src.Busca import *

## Variaveis Constantes
L = 6 # Linhas
C = 6 # Colunas
LARGURA = 800 #largura da tela
ALTURA  = 600 #altura de tela


master = Tk()
master.title("Mapa - IA")
frame = Frame()
frame.pack()
# build do frame


elementos = {'agua' :10, 'floresta': 16}
## define os elementos utilizados e a quantia

mapa = Mapa("mapa", L, C)
#define o nome do mapa e o tamanho da matriz

matriz = [[0 for x in range(L)] for y in range(C)]
#desenha uma matriz zerada

matriz = Mapa.parametrizar(mapa, matriz, L, C, elementos, [1,1],[2,4]) 
nos, vizinhos = Conversor.toGrafo(matriz)
#parametriza a matriz atribuindo os elementos, pos do jogador e destino
#35 destino 7 jogador
l = Busca.amplitude(0,nos, vizinhos, 7, 16)
print(l)

canvas                      = Canvas(master, width=LARGURA, height=ALTURA)
linhas, colunas             = len(matriz), len(matriz[0])
ret_largura, ret_altura     = LARGURA // linhas, ALTURA // colunas
for x in range(L):
    for y in range(C):
        x0, y0 = x * ret_largura, y * ret_altura
        x1, y1 = x0 + ret_largura-1, y0 + ret_altura-1
        canvas.create_rectangle(x0,y0,x1,y1,fill = matriz[x][y]['cor'], width=0)

canvas.pack()
master.mainloop()
