from collections import defaultdict


class G:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(dict)

    def addEdge(self, u, v, w):

        self.graph[u][v] = w

        # if UG
        self.graph[v][u] = w

    def printG(self):

        for node in self.graph:
            adjList = self.graph[node]
            print(node, adjList)

    def modifiedDFSForAllPathsHelper(self, node, visited, K, path):

        if K <= 0:
            print("Yes")
            return True

        visited[node] = True
        print(node, end=" ")
        path.append(node)
        print(path, K)

        adjList = self.graph[node]
        for adjNode in adjList:
            weight = adjList[adjNode]
            if visited[adjNode] is False:
                if weight > K:
                    return True
                if self.modifiedDFSForAllPathsHelper(
                    adjNode, visited, K - weight, path
                ):
                    return True

        visited[node] = False
        path.pop()
        return False

    def modifiedDFSForAllPaths(self, src, K):

        visited = [False] * self.V
        visited[src] = True
        path = []

        # for node in range(self.V):
        #     if visited[node] == "White":
        #         self.modifiedDFSForAllPathsHelper(node, visited)
        print(self.modifiedDFSForAllPathsHelper(src, visited, K, path))


if __name__ == "__main__":

    g = G(9)
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)

    g.printG()

    g.modifiedDFSForAllPaths(src=0, K=60)
