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

        for node in self.graph:
            adjList = self.graph[node]
            print(node, end=" : ")
            for adjNode in adjList:
                print(adjNode, adjList[adjNode], end=" - ")
            print()

    def printPath(self, src, parent):

        for node in range(self.V):
            currNode = node
            path = [node]
            while parent[node] != -1:
                path.append(parent[node])
                node = parent[node]
            print(currNode, ":", path[::-1])

    def getNearestUnvisitedNode(self, distances, visited):

        minDist, minDistNode = float("inf"), None

        for node in range(self.V):
            if not visited[node] and distances[node] <= minDist:
                minDist = distances[node]
                minDistNode = node

        return minDistNode

    def main(self, u, v, k):
        """
        Question:
        Shortest Path between two nodes wuth K edges

        Approach:
        Traverse all path of length K from u to v,
        Pick the one with min weight.
        """
        if k == 0 and u == v:
            return 0
        elif k == 1 and self.graph[u][v]:
            return self.graph[u][v]
        elif k <= 0:
            return float("inf")

        pathWt = float("inf")

        adjList = self.graph[u]
        for adjNode in adjList:
            if adjNode != u and adjNode != v:  # cycle, smaller path
                edge = self.main(adjNode, v, k - 1)
                pathWt = min(pathWt, graph[u][adjNode] + edge)

        return pathWt


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

    # graph.printG()

    graph.prims(0)
