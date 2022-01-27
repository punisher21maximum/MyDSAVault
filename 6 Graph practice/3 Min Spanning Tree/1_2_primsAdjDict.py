from collections import defaultdict


class G:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(dict)

    def addEdge(self, u, v, wt):
        """
        {
            node1:{
                adjNode1: dist11,
                adjNode2: dist12,...
            },
            node2:{
                adjNode1: dist21,
                adjNode2: dist22,...
            },...
        }
        """

        self.graph[u][v] = wt

        # for undirected graph
        self.graph[v][u] = wt

    def printG(self):

        print(self.graph)
        # for node in self.graph:
        #     adjList = self.graph[node]
        #     print(node, end=" : ")
        #     for adjNode in adjList:
        #         print(adjNode, adjList[adjNode], end=" - ")
        #     print()

    def printMST(self, parent):

        print("Edge\tWeight")
        print(parent)
        for node, prevNode in enumerate(parent):
            if node != 0:
                wt = self.graph[node][prevNode]
                print(prevNode, "-", node, "\t", wt)

    def getNearestUnvisitedNode(self, distances, visited):

        minDist, minDistNode = float("inf"), None

        for node in range(self.V):
            if not visited[node] and distances[node] <= minDist:
                minDist = distances[node]
                minDistNode = node

        return minDistNode

    def prims(self, src=0):
        """
        Approach:
        Maintain two sets, mstSet and remainingVertices
        mstSet: has vertices added to MST
        remainingVertices: initially contains all the vertices

        mstSet: nodes are added to mstSet
        remainingVertices: removed from remainingVertices
        """
        visited = [False] * self.V
        distances = [float("inf")] * self.V  # dist from MST of other vertices

        distances[src] = 0

        # path
        parent = [None] * self.V
        parent[src] = src

        for _ in range(self.V):  # V : to add N vertices

            # find nearest node
            node = self.getNearestUnvisitedNode(distances, visited)

            # mark visited
            visited[node] = True

            # updated distances of unvisited
            adjList = self.graph[node]
            for adjNode in adjList:
                wt = adjList[adjNode]
                if not visited[adjNode] and distances[adjNode] > wt:
                    distances[adjNode] = wt
                    parent[adjNode] = node

        self.printMST(parent)


if __name__ == "__main__":

    graph = G(9)
    graph.addEdge(0, 1, 4)
    graph.addEdge(0, 7, 8)
    graph.addEdge(1, 2, 8)
    graph.addEdge(1, 7, 11)
    graph.addEdge(2, 3, 7)
    graph.addEdge(2, 8, 2)
    graph.addEdge(2, 5, 4)
    graph.addEdge(3, 4, 9)
    graph.addEdge(3, 5, 14)
    graph.addEdge(4, 5, 10)
    graph.addEdge(5, 6, 2)
    graph.addEdge(6, 7, 1)
    graph.addEdge(6, 8, 6)
    graph.addEdge(7, 8, 7)

    graph.printG()

    # graph.prims(0)
