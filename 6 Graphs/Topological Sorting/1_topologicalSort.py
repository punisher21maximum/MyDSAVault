

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

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

# code

    def topologicalSortHelper(self, node, visited, topologicalOrder=[]):
        '''
        Topological sort only for Directed Acyclic Graph
        '''

        visited[node] = True

        print(node, end=' ')

        adjacencyList = self.graph[node]
        for adjNode in adjacencyList:
            if not visited[adjNode]:
                self.topologicalSortHelper(adjNode, visited, topologicalOrder)

        topologicalOrder.insert(0, node)

        return topologicalOrder

    def topologicalSort(self):

        visited = [False] * len(self.graph)
        topologicalOrder = []

        for node in self.graph:  # range(len(self.graph)):
            if not visited[node]:
                topologicalOrder = self.topologicalSortHelper(node, visited)

        print(topologicalOrder)


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

    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    # graph.printG()

    print()
    g.topologicalSort()
