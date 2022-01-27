from collections import defaultdict


class G:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)

        # if UG
        self.graph[v].append(u)

    def printG(self):

        for node in self.graph:
            adjList = self.graph[node]
            print(node, adjList)

    def modifiedDFSForAllPathsHelper(self, node, dest, visited, path):

        visited[node] = True
        path.append(node)

        if node == dest:
            print("dest", path)
        else:
            adjList = self.graph[node]
            for adjNode in adjList:
                if visited[adjNode] is False:
                    self.modifiedDFSForAllPathsHelper(adjNode, dest, visited, path)

        path.pop()
        visited[node] = False

    def modifiedDFSForAllPaths(self, src, dest):

        visited = [False] * self.V
        # visited[src] = True
        path = []

        # for node in range(self.V):
        #     if visited[node] == "White":
        #         self.modifiedDFSForAllPathsHelper(node, visited)
        self.modifiedDFSForAllPathsHelper(src, dest, visited, path)


if __name__ == "__main__":

    g = G(9)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)

    g.printG()

    g.modifiedDFSForAllPaths(2, 3)
