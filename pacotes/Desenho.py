from pacotes.Elementos import *
from pacotes.Ambiente import * #Implantada na v1.2
import copy

#Instancia o objeto Elementos com todas suas informações
e = Elementos()

elementos       = e.elementos       #nome dos elementos em si
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

    #DESCOMENTAR O TRECHO ABAIXO PARA CRIAÇÃO MANUAL DO MAPA
    '''for i, x in enumerate(elementos):
        el = input("Insira o nome do elemento " + str(i + 1) + " :").lower()
        validaElemento(i, el, listaElementos)
    corrigePosicaoElementos(listaElementos)'''
    listaElementos = ["montanha", "floresta", "colina", "gelo", "mar", "agua", "solo", "areia"]

    # Usuário insere a quantidade de cada elemento de acordo com a listaElementos

    # DESCOMENTAR O TRECHO ABAIXO PARA CRIAÇÃO MANUAL DO MAPA
    '''casas = m1 * m2
    print("\nVocê possui " + str(casas) + " casas para preencher\n")
    for i, x in enumerate(listaElementos):
        vEl = int(input("Insira a quantidade de campos para o elemento " + str(x) + ":"))
        valorElemento.append(vEl)
        casas -= vEl
        print("\nVocê possui " + str(casas) + " casas para preencher\n")'''
    valorElemento = [55, 35, 45, 25, 60, 40, 100 , 40]

    return valorElemento, listaElementos


#Insere os elementos, bem como suas cores e casas no mapa
def setaElementosMapa(matriz, m1, m2):
    matrizAmbiente                  = copy.deepcopy(matriz) #Cria a matriz do ambiente, para futuras interações entre robo e ambiente.
    contaCasas                      = 0 #Contador para verificar se a quantidade de casas ocupadas pelo elemento não é maior que a quantidade de casas que ele pode ocupar no vetor.
    contaCasasOcupadas              = 0 #Contador para verificar se a quantidade de casas ocupadas pelo elemento não é maior que a quantidade de casas que o usuário inseriu
    contaElemento                   = 0 #Contador para ver qual elemento deve ser pintado na matriz.
    terminou                        = False  # Validador para encerrar os preenchimentos na matriz.
    valorElemento, listaElementos   = defineValoresElementos(m1, m2) #Recebe os valores dos elementos, bem como a lista de elementos ordenada.

    #Para melhor iteragir com a matriz, foram definidos valores de x e y e usado um laço 'while'
    y                               = 0
    x                               = 0

    #Preenche as linhas da matriz
    while x < m1:
        #Preenche as colunas da matriz
        while y < m2:
            if terminou:
                x = m1
                y = m2
                break
            #================================================#
            # Execução do algoritmo de preenchimento do mapa #
            #================================================#
            x, y, m1, m2, matriz,\
            matrizAmbiente, contaElemento,\
            contaCasas, contaCasasOcupadas, \
            listaElementos, \
            valorElemento, terminou = pintaBlocos(x, y, m1, m2, matriz, matrizAmbiente, contaElemento,
                                                  contaCasas, contaCasasOcupadas, listaElementos, valorElemento,
                                                  terminou)



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


#=============================================================#
#Início Métodos de preenchimentos dos blocos da matriz v1.2.0 #
#=============================================================#

#=====================================================================================#
# Verifica se a matrix[x][y] esta com y == m2, ou seja se ela está no final da matriz #
#=====================================================================================#
def verificaUltimaColuna(x, y, m2, contaCasas):
    # Se o y atingir o final do vetor, ele pula a linha, zera o y e zera o contaCasas
    if y == m2:
        x          += 1
        y           = 0
        contaCasas  = 0

    return x, y, contaCasas

#=============================================================================================#
# Verifica se a matriz[x][y] esta com x == m2 e y == m2, ou seja, ultima linha, ultima coluna #
#=============================================================================================#
def verificaUltimaLinhaUltimaColuna(x, y, m2, contaElemento, listaElementos, contaCasasOcupadas, valorElemento, matrizAmbiente,
                                    contaCasas, terminou):
    # Se tanto x, quanto y atingirem o final da matriz (ultima linha, ultima coluna)
    if x == m2 - 1 and y == m2 - 1:
        # Verifica se todos os elementos foram preenchidos
        if contaElemento >= len(listaElementos) - 1:
            # Caso sim, ele verifica se faltam casas para ser ocupadas do ultimo elemento
            if contaCasasOcupadas <= valorElemento[contaElemento]:
                x = 0
                y = 0
            # Caso não, ele encerra o programa
            else:
                terminou = True
                Ambiente(matrizAmbiente)
        # Caso todos os elementos não foram preenchidos, ele volta uma linha, zera o y e zera o contaCasas
        else:
            x -= 1
            y = 0
            contaCasas = 0

    return x, y, terminou, contaCasas

#==================================================================#
# Verifica se apenas x == m2, ou seja, se ela esta na ultima linha #
#==================================================================#
def verificaUltimaLinha(x, m2, contaCasasOcupadas, valorElemento, listaElementos, contaElemento, contaCasas):
    # Verifica se x esta na ultima linha da matriz
    if x == m2 - 1:
        # Verifica se todas as casas do elemento foram ocupadas, se sim, zera o contaCasas
        if contaCasasOcupadas <= valorElemento[contaElemento]:
            if contaCasas <= tamanhoMaximo[0][listaElementos[contaElemento]]:
                x = 0
                y = 0
                contaCasas = 0
            else:
                contaCasas = 0
        # Se não, volta uma linha e zera o contaCasas
        else:
            x -= 1
            contaCasas = 0

    return x, contaCasas
#=========================================================================================================#
# Verifica quantas casas o elemento já ocupou a fim de validar o tamanho máximo de cada elemento no vetor #
#=========================================================================================================#
def verificaContaCasas(contaCasas, listaElementos, contaElemento, x, y):
    # Se o contaCasas atingir o tamanho máximo no vetor, zera o y, pula uma linha e zera o contaCasas
    if contaCasas == tamanhoMaximo[0][listaElementos[contaElemento]]:
        y           -= y
        x           += 1
        contaCasas   = 0

    return x, y, contaCasas

#==================================================================================================================#
# Verifica quantas casas o elemento já ocupou a fim de validar se ele já ocupou a quantidade proposta pelo usuário #
#==================================================================================================================#
def verificaContaCasasOcupadas(contaCasasOcupadas, valorElemento, contaElemento, listaElementos, matrizAmbiente,
                               x, contaCasas, terminou):
    # Verifica se o contaCasas ocupadas é maior ou igual ao valor do elemento proposto pelo usuário
    if contaCasasOcupadas >= valorElemento[contaElemento]:
        # Verifica se é o utlimo elemento, se sim, termina o programa
        if contaElemento >= len(listaElementos) - 1:
            terminou = True
            Ambiente(matrizAmbiente)
        # Se não, 0 o x a fim de procurar quais blocos ainda não foram preenchidos para o próximo elemento
        else:
            x                       = 0
            contaElemento          += 1
            contaCasasOcupadas      = 0
            contaCasas              = 0

    return terminou, matrizAmbiente, x, contaElemento, contaCasasOcupadas, contaCasas

#====================================================#
# Busca o próximo bloco neutro, ou seja, bloco cinza #
#====================================================#
def buscaBlocoNeutro(x, y, m1, m2, contaCasasOcupadas, valorElemento, contaElemento, contaCasas):
    y += 1
    # Se o y chegar na ultima coluna
    if y == m2:
        # Verifica se não estão todas as casas ocupadas
        if y >= m1 - 1 and x >= m2 - 1 and contaCasasOcupadas <= valorElemento[contaElemento]:
            x = 0
            y = 0
        # Se não, pula uma linha, zera o y e 0 o contaCasas
        else:
            x += 1
            y = 0
            contaCasas = 0

    return x, y, contaCasas

#====================================================================================#
#Pinta os blocos da matriz executando todos os métodos de validação de preenchimento #
#====================================================================================#
def pintaBlocos(x, y, m1 , m2, matriz, matrizAmbiente, contaElemento, contaCasas, contaCasasOcupadas,
                listaElementos, valorElemento, terminou):
    # Se a posição for cinza ele pinta com a outra cor
    if matriz[x][y] == "gray":
        matrizAmbiente[x][y] = elementos[contaElemento]
        matriz[x][y] = cores[0][elementos[contaElemento]]
        contaCasas += 1
        contaCasasOcupadas += 1

        x, y, contaCasas                    = verificaUltimaColuna(x, y, m2, contaCasas)
        x, y, terminou, contaCasas          = verificaUltimaLinhaUltimaColuna(x, y, m2, contaElemento, listaElementos,
                                                                                contaCasasOcupadas, valorElemento,
                                                                                matrizAmbiente, contaCasas, terminou)

        x, contaCasas                       = verificaUltimaLinha(x, m2, contaCasasOcupadas,
                                                                  valorElemento, listaElementos, contaElemento,
                                                                  contaCasas)

        x, y, contaCasas                    = verificaContaCasas(contaCasas, listaElementos, contaElemento, x, y)

        terminou, matrizAmbiente, \
        x, contaElemento, contaCasasOcupadas, \
        contaCasas                          = verificaContaCasasOcupadas(contaCasasOcupadas, valorElemento,
                                                                            contaElemento, listaElementos,
                                                                         matrizAmbiente,
                                                                        x, contaCasas, terminou)


    # Se a cor não for cinza, vai pulando de bloco até encontrar um bloco cinza através do método buscaBlocoNeutro
    else:
        x, y, contaCasas = buscaBlocoNeutro(x, y, m1, m2, contaCasasOcupadas, valorElemento,
                                            contaElemento, contaCasas)


    return x, y, m1 , m2, matriz, matrizAmbiente, contaElemento, contaCasas, contaCasasOcupadas,\
           listaElementos,\
           valorElemento, terminou





