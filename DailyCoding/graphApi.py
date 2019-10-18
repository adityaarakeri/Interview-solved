'''
Graph API to contruct dense graph using Graph class which inherits vertex class.
'''


'''
Vertex class to create each vertex of the graph, which has following method

addNeighbor - adding nearest vertices to the selected vertex with edge weight
getConnections - getting all the vertices connected to a vertex
getId - getting id of the vertex
getWeight - getting weight of the edge from the vertex and nbr

'''

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


'''
Graph class to define graph with following methods -

addVertex - adding vertex to graph
getVertex - get the vertex from vertList
addEdge - adding edge between u and v with weight w
getVertices - get all the keys of vertList

'''

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

# Initializing a graph
g = Graph()

# adding vertices to the graph g
for i in range(6):
    g.addVertex(i)

# View all the added vertices
print(g.vertList)