#CONJUNTO

class no:
    def __init__(self,lista_arestas,vertices):
        self.arestas = lista_arestas
        self.vertices = vertices
class Grafo:
    def __init__(self, arestas, vertices):
        self.arestas = arestas
        self.vertices = vertices
        self.inicio = None
    def busca(self,Q,vertice):
        for i in Q:
            for elemento in i:
                if elemento == vertice:
                    return i
    def uniao(self, Q, u, v):
        uniao1 = self.busca(Q,u)
        uniao2 = self.busca(Q,v)
        if len(uniao2)> 1:
            for i in uniao2:
                Q[Q.index(uniao1)].append(i)
        else:
            Q[Q.index(uniao1)].append(v)
        Q.pop(Q.index(uniao2))
        return Q
    def linka(self):
        Q = []
        for v in self.vertices:
            Q.append([v])
        for edge in self.arestas:
            if self.busca(Q,edge[0]) != self.busca(Q,edge[1]):
                aux = self.uniao(Q,edge[0],edge[1])
                Q = aux
        return len(Q)
entr1 = input().split()
n = int(entr1[0])
cont = 0
aresta,vertice = [],[]
for i in range(1, n+1):
    i = int(i)
    vertice.append(i)
while cont<int(entr1[1]):
    entr2 = input().split()
    e = (int(entr2[0]),int(entr2[1]))
    aresta.append(e)
    cont += 1
grafo = Grafo(aresta,vertice)
familias = grafo.linka()
print(familias)










