

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

    def traverseBFS(self, src):

        visited = [False] * (max(self.graph) + 1)

        queue = [src]
        visited[src] = True

        while queue:
            nodeData = queue.pop(0)

            print(nodeData, end=' ')

            for neighbourNode in self.graph[nodeData]:
                if not visited[neighbourNode]:
                    queue.append(neighbourNode)
                    visited[neighbourNode] = True


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
