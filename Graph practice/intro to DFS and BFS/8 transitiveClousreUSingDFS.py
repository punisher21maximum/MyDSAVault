from collections import defaultdict


class G:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):

        self.graph[src].append(dest)

        # for undirected graph
        # self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

    def DFS(self, u, v):

        if u == v and u in self.graph[u]:
            self.transitiveClosure[u][u] = 1
        else:
            self.transitiveClosure[u][v] = 1

            adjList = self.graph[v]
            for adjNode in adjList:
                if self.transitiveClosure[u][adjNode] == 0:
                    self.DFS(u, adjNode)

    def getTransistiveClosureUsingDFS(self):

        self.transitiveClosure = [[0] * self.V for _ in range(self.V)]

        for node in self.graph:
            self.DFS(node, node)

        print(self.transitiveClosure)


if __name__ == "__main__":

    g = G(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    # graph.printG()

    g.getTransistiveClosureUsingDFS()
