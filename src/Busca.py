from src.Lista import Lista


class Busca:

    def amplitude(self, nos, vizinhos, inicio, fim):
        inicio = nos[inicio]
        fim = nos[fim]
        l1 = Lista()
        l2 = Lista()
        visitado = []
        l1.add(inicio, None, 0)
        l2.add(inicio, None, 0)
        visitado.append(inicio)
        achou = False

        while l1.isEmpty() is not None and not achou:
            atual = l1.removeFirst()
            indice = atual.valor['identificador']
            for i in range(len(vizinhos[indice])):
                novo = vizinhos[indice][i]
                flag = True

                for j in range(len(visitado)):
                    if visitado[j]['identificador'] == novo['identificador']:
                        flag = False
                        break

                if flag:
                    l1.add(novo, atual, 0)
                    l2.add(novo, atual, 0)
                    visitado.append(novo)

                    if novo['identificador'] == fim['identificador']:
                        caminho = []
                        caminho = l2.showTree()
                        return caminho

    def profundidade(self, nos, vizinhos, inicio, fim):
        inicio = nos[inicio]
        fim = nos[fim]
        l1 = Lista()
        l2 = Lista()
        visitado = []
        l1.add(inicio, None, 0)
        l2.add(inicio, None, 0)
        visitado.append(inicio)
        achou = False

        while l1.isEmpty() is not None and not achou:
            atual = l1.removeLast()
            indice = atual.valor['identificador']
            for i in range(len(vizinhos[indice])):
                novo = vizinhos[indice][i]
                flag = True
                for j in range(len(visitado)):
                    if visitado[j]['identificador'] == novo['identificador']:
                        flag = False
                        break

                if flag:
                    l1.add(novo, atual, atual.nivel + 1)
                    l2.add(novo, atual, atual.nivel + 1)
                    visitado.append(novo)
                if novo['identificador'] == fim['identificador']:
                    caminho = []
                    caminho = l2.showTree()
                    return caminho

    def profundidadeLimite(self, nos, vizinhos, inicio, fim, limite):
        inicio = nos[inicio]
        fim = nos[fim]
        l1 = Lista()
        l2 = Lista()
        visitado = []
        l1.add(inicio, None, 0)
        l2.add(inicio, None, 0)
        visitado.append(inicio)
        achou = False

        while l1.isEmpty() is not None and not achou:
            atual = l1.removeLast()
            indice = atual.valor['identificador']
            if(limite != atual.nivel):
                for i in range(len(vizinhos[indice])):
                    novo = vizinhos[indice][i]
                    flag = True
                    for j in range(len(visitado)):
                        if visitado[j]['identificador'] == novo['identificador']:
                            flag = False
                            break

                    if flag:
                        l1.add(novo, atual, atual.nivel + 1)
                        l2.add(novo, atual, atual.nivel + 1)
                        visitado.append(novo)
                    if novo['identificador'] == fim['identificador']:
                        caminho = []
                        caminho = l2.showTree()
                        return caminho
            else:
                return 'Atingiu o valor limite, impossivel chegar no valor'

    def aprofundamentoInterativo(self, nos, vizinhos, inicio, fim):
        inicio = nos[inicio]
        fim = nos[fim]
        l1 = Lista()
        l2 = Lista()
        visitado = []
        l1.add(inicio, None, 0)
        l2.add(inicio, None, 0)
        visitado.append(inicio)
        achou = False
        for limite in range(len(nos)):
            while l1.isEmpty() is not None and not achou:
                atual = l1.removeLast()
                indice = atual.valor['identificador']
                if(limite != atual.nivel):
                    for i in range(len(vizinhos[indice])):
                        novo = vizinhos[indice][i]
                        flag = True
                        for j in range(len(visitado)):
                            if visitado[j]['identificador'] == novo['identificador']:
                                flag = False
                                break

                        if flag:
                            l1.add(novo, atual, atual.nivel + 1)
                            l2.add(novo, atual, atual.nivel + 1)
                            visitado.append(novo)
                        if novo['identificador'] == fim['identificador']:
                            caminho = []
                            caminho = l2.showTree()
                            return caminho
