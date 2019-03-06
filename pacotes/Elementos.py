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
        3: "gelo",
        4: "mar",
        5: "colina",
        6: "montanha",
        7: "areia"
    }

    return elementos


#define o tamanho máximo de cada elemento através de um dicionário
def defineTamanhoMaximo():
    tamanhoMaximo = [dict(
                          agua              =5,
                          solo              =8,
                          floresta          =6,
                          gelo              =4,
                          mar               =6,
                          colina            =4,
                          montanha          =7,
                          areia             =5)]
    return tamanhoMaximo


#define as cores dos elementos
def defineCores():
    agua            = "#3087C1"
    solo            = "#EDE29C"
    floresta        = "#129B00"
    gelo            = "#8BF1E8"
    mar             = "#001773"
    colina          = "#088A68"
    montanha        = "#5F4C0B"
    areia           = "#F5F6CE"

    cores = [dict(
                  agua          =agua,
                  solo          =solo,
                  floresta      =floresta,
                  gelo          =gelo,
                  mar           =mar,
                  colina        =colina,
                  montanha      =montanha,
                  areia         =areia)]

    return cores


#define os pesos dos elementos
def definePesos():
    pesos = [dict(
        agua            =1.5,
        solo            =1,
        floresta        =2.5,
        gelo            =4,
        mar             =6,
        colina          =4,
        montanha        =7,
        areia           =3.5
    )]

    return pesos