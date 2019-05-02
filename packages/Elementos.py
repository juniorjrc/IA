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
        0: "BRISTOL_HILLS",
        1: "SOUTH_ISLAND",
        2: "NORTH_ISLAND",
        3: "TRICORNER_YARDS",
        4: "PARKVILLE",
        5: "NARROWS",
        6: "BLACK_GATE",
        7: "HAYSVILLE"
    }

    return elementos

#define o tamanho máximo de cada elemento através de um dicionário
def defineTamanhoMaximo():
    tamanhoMaximo = [dict(
                          BRISTOL_HILLS                 =5,
                          SOUTH_ISLAND                  =8,
                          NORTH_ISLAND                  =6,
                          TRICORNER_YARDS               =4,
                          PARKVILLE                     =6,
                          NARROWS                       =4,
                          BLACK_GATE                    =7,
                          HAYSVILLE                     =5)]
    return tamanhoMaximo


#define as cores dos elementos
def defineCores():
    BRISTOL_HILLS               = "#151515"
    SOUTH_ISLAND                = "#1C1C1C"
    NORTH_ISLAND                = "#2E2E2E"
    TRICORNER_YARDS             = "#424242"
    PARKVILLE                   = "#585858"
    NARROWS                     = "#6E6E6E"
    BLACK_GATE                  = "#000000"
    HAYSVILLE                   = "#848484"

    cores = [dict(
                  BRISTOL_HILLS             =BRISTOL_HILLS,
                  SOUTH_ISLAND              =SOUTH_ISLAND,
                  NORTH_ISLAND              =NORTH_ISLAND,
                  TRICORNER_YARDS           =TRICORNER_YARDS,
                  PARKVILLE                 =PARKVILLE,
                  NARROWS                   =NARROWS,
                  BLACK_GATE                =BLACK_GATE,
                  HAYSVILLE                 =HAYSVILLE)]

    return cores


#define os pesos dos elementos
def definePesos():
    pesos = [dict(
        BRISTOL_HILLS               =1.5,
        SOUTH_ISLAND                =1,
        NORTH_ISLAND                =2.5,
        TRICORNER_YARDS             =3,
        PARKVILLE                   =2,
        NARROWS                     =4,
        BLACK_GATE                  =200,
        HAYSVILLE                   =3.5
    )]

    return pesos