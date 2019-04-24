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
                        caminho = caminho[::-1]
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
                    caminho = caminho[::-1]
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
                        caminho = caminho[::-1]
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

    def bidirecional(self, nos, vizinhos, inicio, fim):
        inicio = nos[inicio]
        fim = nos[fim]

        l1 = Lista()
        l2 = Lista()
        l3 = Lista()
        l4 = Lista()
        visitado = []

        l1.add(inicio, None, 0)
        l2.add(inicio, None, 0)
        linha = []
        linha.append(inicio)
        linha.append(1)
        visitado.append(linha)

        l3.add(fim, None, 0)
        l4.add(fim, None, 0)
        linha = []
        linha.append(inicio)
        linha.append(2)
        visitado.append(linha)

        while True:

            flag1 = True
            while flag1:
                atual = l1.removeFirst()
                indice = atual.valor['identificador']
                for i in range(len(vizinhos[indice])):
                    novo = vizinhos[indice][i]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visitado)):
                        if visitado[j][0]['identificador'] == novo['identificador']:
                            if visitado[j][1] == 1:
                                flag2 = False
                            else:
                                flag3 = True
                            break

                    if flag2:
                        l1.add(novo, atual, atual.nivel + 1)
                        l2.add(novo, atual, atual.nivel + 1)

                        if flag3:
                            caminho = []
                            caminho = l2.showTree()
                            caminho = caminho[::-1]
                            caminho += l4.showTree1(novo)
                            return caminho
                        else:
                            linha = []
                            linha.append(novo)
                            linha.append(1)
                            visitado.append(linha)
                if l1.isEmpty() != True:
                    aux = l1.first()
                    if atual.nivel == aux.nivel:
                        flag1 = True
                    else:
                        flag1 = False

            flag1 = True
            while flag1:
                atual = l3.removeFirst()
                indice = atual.valor['identificador']

                for i in range(len(vizinhos[indice])):
                    novo = vizinhos[indice][i]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visitado)):
                        if visitado[j][0]['identificador'] == novo['identificador']:
                            if visitado[j][1] == 2:
                                flag2 = False
                            else:
                                flag3 = True
                            break

                    if flag2:
                        l3.add(novo, atual, atual.nivel + 1)
                        l4.add(novo, atual, atual.nivel + 1)

                        if flag3:
                            caminho = []
                            caminho = l4.showTree()
                            caminho = caminho[::-1]
                            caminho += l2.showTree1(novo)
                            return caminho
                        else:
                            linha = []
                            linha.append(novo)
                            linha.append(2)
                            visitado.append(linha)
                if l3.isEmpty() != True:
                    aux = l3.first()
                    if atual.nivel == aux.nivel:
                        flag1 = True
                    else:
                        flag1 = False            
