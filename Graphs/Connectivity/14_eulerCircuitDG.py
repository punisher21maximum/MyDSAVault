from collections import defaultdict


class G:

    def __init__(self, V):

        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)

    def printG(self):

        for node in self.graph:
            print(node, ':', self.graph[node])

    def transposeOfAdjListGraph(self):

        transposeG = G(self.V)

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

    def isAllNonZeroDegreeVerticesBelongToOneComponent(self):

        vertex = 0

        visited = [False] * self.V

        self.DFSwithSrcV1(vertex, visited)

        for node in range(self.V):
            adjList = self.graph[node]
            if not visited[node] and len(adjList) > 0:
                print('Not Strongly Connected')
                return False

        transposeG = self.transposeOfAdjListGraph()

        visited = [False] * transposeG.V

        transposeG.DFSwithSrcV1(vertex, visited)

        for node in range(transposeG.V):
            adjList = self.graph[node]
            if not visited[node] and len(adjList) > 0:
                print('Not Strongly Connected')
                return False

        print('Strongly Connected')
        return True

    def isIndegreeAndOutdegreeEqualForAllNodes(self):

        inDegree, outDegree = [0] * self.V, [0] * self.V

        for node in self.graph:
            adjList = self.graph[node]

            outDegree[node] = len(adjList)

            for adjNode in adjList:
                inDegree[adjNode] += 1

        for node in range(self.V):
            if inDegree[node] != outDegree[node]:
                print('Degree Mismatch')
                return False

        print('Degrees Matched')
        return True

    def isEulerCircuitDG(self):
        '''
        Euler Circuit:
        1. All non-zero degree vertices belong to 1
        strongly connected component
        2. For all vertices, in-degree equal to out-degree
        '''

        if (self.isAllNonZeroDegreeVerticesBelongToOneComponent()
                and self.isIndegreeAndOutdegreeEqualForAllNodes()):
            print('Eulerian Circuit')
        else:
            print('Non Eulerian Circuit')


if __name__ == '__main__':

    g = G(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 0)

    # g.printG()

    g.isEulerCircuitDG()
