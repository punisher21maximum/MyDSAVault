

class G:

    def __init__(self):
        self.graph = dict()

    def addEdge(self, src, dest, weight):

        if src not in self.graph:
            self.graph[src] = []
        if dest not in self.graph:
            self.graph[dest] = []

        self.graph[src].append([dest, weight])

        # for undirected graph
        # if src != dest:
        #     self.graph[dest].append([src, weight])

        self.V = len(self.graph)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

# Code

    def floydWarshallDetectNegativeCycle(self, src):

        distances = [float('inf')] * len(self.V)
        distances[src] = 0
        visited = [False] * len(self.V)

        for node in self.graph:
            if not visited[node]:
                visited[node] = True

                adjList = self.graph[node]
                for adjNode, distFromNodeToAdjNode in adjList:

                    if distances[adjNode] > distances[node] + distFromNodeToAdjNode:
                        distances[adjNode] = distances[node] + \
                            distFromNodeToAdjNode
            else:
                print(distances[adjNode])


if __name__ == "__main__":

    g = G()

    g.addEdge(0, 0, 0)
    g.addEdge(0, 1, 1)
    g.addEdge(1, 1, 0)
    g.addEdge(1, 2, -1)
    g.addEdge(2, 2, 0)
    g.addEdge(2, 3, -1)
    g.addEdge(3, 3, 0)
    g.addEdge(3, 0, -1)

    g.printG()

    # print(g.floydWarshallDetectNegativeCycle(0))
