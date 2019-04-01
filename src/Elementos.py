
class Elementos:

    @staticmethod
    def get():
        elementos = {
            'jogador':{
                'nome':'jogador',
                'cor': '#FFFFFF',
                'peso':0
                },
            'destino':{
                'nome':'destino',
                'cor': '#000000',
                'peso':0
                },
            'agua':{
                    'nome': 'agua',
                    'max': 6,
                    'cor': '#3087C1',
                    'peso': 3
                },
            'solo':{
                    'nome':'solo',   
                    'max': 10,
                    'cor': '#B0DB9C',
                    'peso': 1
                },
            'floresta':{
                    'nome':'floresta',
                    'max': 5,
                    'cor': '#129B00',
                    'peso': 2
                }
            }

        return elementos
        
