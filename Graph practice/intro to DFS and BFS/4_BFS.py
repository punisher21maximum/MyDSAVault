

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

    def traverseBFS(self, srcNode):

        visited = [False] * len(self.graph)

        queue = [srcNode]
        while queue:
            node = queue.pop(0)

            visited[node] = True
            print(node, end=' ')

            adjList = self.graph[node]
            for i in range(len(adjList)):
                adjNode = adjList[i]
                if not visited[adjNode]:
                    queue.append(adjNode)

    def traverseDFS(self, srcNode):

        visited = [False] * len(self.graph)

        queue = [srcNode]
        while queue:
            node = queue.pop()

            visited[node] = True
            print(node, end=' ')

            adjList = self.graph[node]
            for i in range(len(adjList)):
                adjNode = adjList[i]
                if not visited[adjNode]:
                    queue.append(adjNode)


if __name__ == "__main__":

    g = G()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(2, 6)
    g.addEdge(3, 7)
    g.addEdge(3, 8)
    g.addEdge(4, 9)
    g.addEdge(4, 10)

    # graph.printG()

    g.traverseBFS(0)
