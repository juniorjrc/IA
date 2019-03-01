from pacotes.Elementos import *
#Instancia o objeto Elementos com todas suas informações
e = Elementos()

elementos       = e.elementos[0]    #nome dos elementos em si
tamanhoMaximo   = e.tamanhoMaximo   #tamanho maximo de cada elemento
cores           = e.cores           #cores dos elementos
pesos           = e.pesos           #pesos dos elementos

#Método de definição da grade de ocupação dos elementos na matriz
#Usuário insere ordem aos elementos e posteriormente seus valores
def defineValoresElementos(m1, m2):
    listaElementos  = []  # Lista dos elementos
    valorElemento   = []  # valor das quantidades de cada elemento

    mostraInterfaceApresentacao()

    # Usuário insere a ordem dos elementos por nome
    for i, x in enumerate(elementos):
        el = input("Insira o nome do elemento " + str(i + 1) + " :").lower()
        validaElemento(i, el, listaElementos)

    corrigePosicaoElementos(listaElementos)

    # Usuário insere a quantidade de cada elemento de acordo com a listaElementos
    casas = m1 * m2
    print("\nVocê possui " + str(casas) + " casas para preencher\n")
    for i, x in enumerate(listaElementos):
        vEl = int(input("Insira a quantidade de campos para o elemento " + str(x) + ":"))
        valorElemento.append(vEl)
        casas -= vEl
        print("\nVocê possui " + str(casas) + " casas para preencher\n")

    return valorElemento


#Insere os elementos, bem como suas cores e casas no mapa
def setaElementosMapa(matriz, m1, m2):
    contaCasas      = 0
    contaElemento   = 0
    valorElemento   = defineValoresElementos(m1, m2)

    #Preenche as colunas da matriz
    for x in range(m1):
        #Preenche as linhas da matriz
        for y in range(m2):
            if valorElemento[contaElemento] > contaCasas: #Verifica se a a quantidade de quadrados ocupados pelo elemento é > que a quantidade que o usuário inseriu
                matriz[x][y]    = cores[0][elementos[contaElemento]]
                contaCasas      += 1
            else:
                if contaElemento >= len(valorElemento) -1:#Verifica se sobrou quadrados no mapa, se sim, pinta de cinza
                    matriz[x][y] = "gray"
                else:
                    contaCasas      = 0
                    matriz[x][y]    = cores[0][elementos[contaElemento + 1]]
                    contaCasas      += 1
                    contaElemento   += 1


#Valida se o elemento existe na lista de elementos, bem como se ele já não foi inserido duas vezes
def validaElemento(i, el, listaElementos):
    if el in elementos.values() and el not in listaElementos:
        listaElementos.append(el)
    else:
        while el not in elementos.values() or el in listaElementos:
            print("Elemento desconhecido ou já consta na lista de elementos do mapa")
            el = input("Insira o nome do elemento " + str(i + 1) + " :").lower()
        listaElementos.append(el)


#Corrige a posição dos elementos para pegar suas cores
def corrigePosicaoElementos(listaElementos):
    elementos.clear()
    for x, y in enumerate(listaElementos):
        elementos[x] = y

    return elementos


#Mostra interface de início
def mostraInterfaceApresentacao():
    print("#========================================#")
    print("    ELEMENTOS DISPONÍVEIS PARA O MAPA    ")
    for i, x in enumerate(elementos):
        print("    " + str(elementos[i]).upper())
    print("#========================================#")








