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

    def modifiedDFSForAllPathsHelper(self, node, visited):

        visited[node] = True
        print(node, end=" ")

        adjList = self.graph[node]
        for adjNode in adjList:
            if visited[adjNode] is False:
                self.modifiedDFSForAllPathsHelper(adjNode, visited)

        visited[node] = False

    def modifiedDFSForAllPaths(self, src):

        visited = [False] * self.V
        visited[src] = True

        # for node in range(self.V):
        #     if visited[node] == "White":
        #         self.modifiedDFSForAllPathsHelper(node, visited)
        self.modifiedDFSForAllPathsHelper(src, visited)


if __name__ == "__main__":

    g = G(4)
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(0, 3)
    # g.addEdge(0, 4)
    # g.addEdge(1, 2)
    # g.addEdge(1, 5)
    # g.addEdge(2, 3)
    # g.addEdge(2, 5)
    # g.addEdge(3, 4)
    # g.addEdge(3, 5)
    # g.addEdge(4, 5)

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(1, 3)
    g.addEdge(2, 1)
    g.addEdge(2, 3)

    g.printG()

    g.modifiedDFSForAllPaths(0)
