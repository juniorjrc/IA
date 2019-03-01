class Elementos:
    #Método construtor
    def __init__(self):
        self.elementos = defineElementos()
        self.tamanhoMaximo = defineTamanhoMaximo()
        self.cores = defineCores()
        self.pesos = definePesos()


#define os elementos através de um dicionário
def defineElementos():
    elementos = {
        0: "agua",
        1: "solo",
        2: "floresta",
        3: "montanha",
        4: "grama"
    }

    agentes ={
        0: "jogador",
        1: "destino"
    }

    return elementos, agentes


#define o tamanho máximo de cada elemento através de um dicionário
def defineTamanhoMaximo():
    tamanhoMaximo = [dict(jogador           =1,
                          destino           =1,
                          agua              =5,
                          solo              =8,
                          floresta          =6,
                          montanha          =7,
                          grama             =9)]
    return tamanhoMaximo


#define as cores dos elementos
def defineCores():
    montanha        = "#2A1B0A"
    solo            = "#F4FA58"
    agua            = "blue"
    floresta        = "#0B610B"
    jogador         = "white"
    destino         = "black"
    grama           = "#01DF01"

    cores = [dict(jogador       =jogador,
                  destino       =destino,
                  agua          =agua,
                  solo          =solo,
                  floresta      =floresta,
                  montanha      =montanha,
                  grama         =grama)]

    return cores


#define os pesos dos elementos
def definePesos():
    pesos = [dict(
        jogador         =0,
        destino         =0,
        agua            =5,
        solo            =10,
        floresta        =23,
        montanha        =28,
        grama           =12
    )]

    return pesos