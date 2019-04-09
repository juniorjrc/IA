from src.Lista import Lista

class Busca:


    def amplitude(self, nos, vizinhos, inicio, fim):
        inicio = nos[inicio]
        fim = nos[fim]
        l1 = Lista()
        l2 = Lista()
        visitado = []
        l1.add(inicio,None,0)
        l2.add(inicio,None,0)
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
                    l1.add(novo, atual,0)
                    l2.add(novo, atual,0)
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
        l1.add(inicio,None,0)
        l2.add(inicio,None,0)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        achou = False

        while l1.isEmpty() is not None and not achou:
        atual = l1.removeLast()
        indice = atual.valor['identificador']
        for i in range(len(vizinhos[indice])-1,-1,1):
            novo = vizinhos[indice][i]
            flag = True
            for j in range(len(visitado)):
                if visitado[j]['identificador'] == novo['identificador']:
                        flag = False
                        break

            if flag == False:
                l1.add(novo, atual,atual.nivel + 1)
                l2.add(novo, atual,atual.nivel + 1)

                linha =[]
                linha.append(novo)
                linha.append(atual.nivel+1)

            if novo['identificador'] == fim['identificador']:
                caminho = []
                caminho = l2.showTree()
                return caminho
            
