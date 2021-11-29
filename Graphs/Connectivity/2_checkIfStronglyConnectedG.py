from collections import defaultdict


class Graph:

    def __init__(self, V):

        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)

    def transposeOfAdjListGraph(self):

        transposeG = Graph(self.V)

        for node in self.graph:
            adjList = self.graph[node]
            for adjNode in adjList:
                transposeG.addEdge(adjNode, node)

        return transposeG

    def DFSwithSrcV1(self, vertex, visited):

        visited[vertex] = True

        adjList = self.graph[vertex]
        for adjNode in adjList:
            if not visited[adjNode]:
                self.DFSwithSrcV1(adjNode, visited)

    def isStronglyConnected(self):
        '''
        idea: if any vertex say V1, can reach all other vertices
        and V1 can be reached by all other vertices, then it is 
        strongly connected.

        Algo:
        s1: pick any vertex V1
        s2: DFS with V1 as src, if all other vertices not visited, then return False
        s3: find transpose of graph
        s4: pick same vertex V1 from s1
        s5: DFS with V1 as src, if all other vertices not visited, then return False else True
        '''

        vertex = 0

        visited = [False] * self.V

        self.DFSwithSrcV1(vertex, visited)

        for node in range(self.V):
            if not visited[node]:
                print('Not Strongly Connected')
                return False

        transposeG = self.transposeOfAdjListGraph()

        visited = [False] * transposeG.V

        transposeG.DFSwithSrcV1(vertex, visited)

        for node in range(transposeG.V):
            if not visited[node]:
                print('Not Strongly Connected')
                return False

        print('Strongly Connected')
        return True


if __name__ == '__main__':

    g1 = Graph(5)
    g1.addEdge(0, 1)
    g1.addEdge(1, 2)
    g1.addEdge(2, 3)
    g1.addEdge(3, 0)
    g1.addEdge(2, 4)
    g1.addEdge(4, 2)
    print("Yes" if g1.isStronglyConnected() else "No")

    g2 = Graph(4)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    print("Yes" if g2.isStronglyConnected() else "No")
