

class G:

    def __init__(self):
        self.graph = dict()

    def addEdge(self, src, dest):

        if src not in self.graph:
            self.graph[src] = []
        if dest not in self.graph:
            self.graph[dest] = []

        self.graph[src].append(dest)

        # for undirected graph
        # self.graph[dest].append(src)

        self.V = len(self.graph)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

# Code O(V^2)

    def getReachabilityMatrixHelper(self, node, visited, reachMatrix, i=''):

        reachMatrix[node][node] = 1

        visited[node] = 'Being Visited'

        adjacencyList = self.graph[node]
        for adjNode in adjacencyList:

            reachMatrix[node][adjNode] = 1

            if visited[adjNode] == 'Not Visited':
                print(i+' ', 'adjNode v', adjNode)
                self.getReachabilityMatrixHelper(
                    adjNode, visited, reachMatrix, i+' ')

            for reachableNode in range(self.V):
                if reachMatrix[adjNode][reachableNode] == 1:
                    reachMatrix[node][reachableNode] = 1

        visited[node] = 'Visited'

        return reachMatrix

    def getReachabilityMatrix(self):

        visited = ['Not Visited'] * self.V
        reachMatrix = [[0 for i in range(self.V)] for j in range(self.V)]

        for node in self.graph:
            if visited[node] == 'Not Visited':
                reachMatrix = self.getReachabilityMatrixHelper(
                    node, visited, reachMatrix)

        self.printM(reachMatrix)
        return reachMatrix

    def printM(self, r):
        for i in r:
            print(i)


if __name__ == "__main__":

    g = G()
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 3)
    # g.addEdge(1, 4)
    # g.addEdge(2, 5)
    # g.addEdge(2, 6)
    # g.addEdge(3, 7)
    # g.addEdge(3, 8)
    # g.addEdge(4, 9)
    # g.addEdge(4, 10)

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.printG()

    # node = 2
    # print(g.getReachableNodesFromANode(node, reachableNodes=[node]))

    print(g.getReachabilityMatrix())
