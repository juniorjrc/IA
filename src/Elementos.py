
class Elementos:

    @staticmethod
    def get():
        elementos = {
            'jogador':{
                'identificador': None,
                'nome':'jogador',
                'cor': '#FFFFFF',
                'peso':0
                },
            'destino':{
                'identificador': None,
                'nome':'destino',
                'cor': '#000000',
                'peso':0
                },
            'agua':{
                'identificador': None,
                    'nome': 'agua',
                    'max': 6,
                    'cor': '#3087C1',
                    'peso': 3
                },
            'solo':{
                'identificador': None,
                    'nome':'solo',   
                    'max': 10,
                    'cor': '#B0DB9C',
                    'peso': 1
                },
            'floresta':{
                'identificador': None,
                    'nome':'floresta',
                    'max': 5,
                    'cor': '#129B00',
                    'peso': 2
                },
            'lava': {
                'identificador': None,
                'nome': 'lava',
                'max':10,
                'cor': '#ff3300',
                'peso': 5
            }
            }

        return elementos
        
