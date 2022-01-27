from collections import defaultdict


class G:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):

        self.graph[src].append(dest)

        # if UG
        # self.graph[dest].append(src)

    def printG(self):

        for node in self.graph:
            adjList = self.graph[node]
            print(node, adjList)

    def iterativeDFS(self, src=0):

        visited = [False] * self.V
        print(src, end=" ")
        visited[src] = True
        stack = [src]

        while stack:
            node = stack.pop()

            adjList = self.graph[node]
            for adjNode in adjList:
                if not visited[adjNode]:
                    print(adjNode, end=" ")
                    visited[adjNode] = True
                    stack.append(adjNode)


if __name__ == "__main__":

    g = G(11)
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

    g.printG()

    g.DFS()
