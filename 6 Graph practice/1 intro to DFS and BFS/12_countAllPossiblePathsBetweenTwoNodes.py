

class G:

    def __init__(self, V):
        self.V = V
        self.graph = dict()

    def addEdge(self, src, dest):

        if src not in self.graph:
            self.graph[src] = []
        if dest not in self.graph:
            self.graph[dest] = []

        self.graph[src].append(dest)

        # for undirected graph
        # self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

    def countAllPossiblePathBetweenTwoNodes(self, currNode, destNode, visited, N):
        '''
        Time O(N!)
        '''

        visited[currNode] = True

        if currNode == destNode:
            N += 1
        else:
            adjList = self.graph[currNode]
            for adjNode in adjList:
                if not visited[adjNode]:
                    N = self.countAllPossiblePathBetweenTwoNodes(
                        adjNode, destNode, visited, N
                    )

        visited[currNode] = False

        return N


if __name__ == "__main__":

    g = G(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)

    # graph.printG()
    visited = [False] * 4
    print(g.countAllPossiblePathBetweenTwoNodes(2, 3, visited, 0))
