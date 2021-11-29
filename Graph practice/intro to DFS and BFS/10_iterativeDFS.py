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

    def iterativeDFS(self, node):

        stack = [node]
        visited = [False] * self.V

        while stack:
            node = stack.pop()

            print(node, end=' ')
            visited[node] = True

            adjList = self.graph[node]
            for adjNode in adjList:
                if not visited[adjNode]:
                    stack.append(adjNode)


if __name__ == "__main__":

    g = G(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 4)

    # graph.printG()

    g.iterativeDFS(0)
