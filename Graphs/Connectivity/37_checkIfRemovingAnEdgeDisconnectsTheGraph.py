from collections import defaultdict


class G:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)

        # UG
        self.graph[v].append(u)

    def printG(self):

        for node in self.graph:
            print(node, self.graph[node])

    def isConnected(self, removedEdge, node):

        reachedNodes = []
        visited = [False] * len(self.graph)

        queue = [node]

        while queue:
            node = queue.pop()

            if visited[node]:
                continue
            visited[node] = True

            if node not in reachedNodes:
                reachedNodes.append(node)

            if len(reachedNodes) == len(self.graph):
                return True

            adjList = self.graph[node]
            for adjNode in adjList:
                if node in removedEdge and adjNode in removedEdge:
                    continue
                queue.append(adjNode)

        print(reachedNodes)
        return False

    def checkIfRemovingAGivenEdgeDisconnectsGraph(self):

        bridgeEdges = []

        for node in self.graph:

            adjList = self.graph[node]
            for adjNode in adjList:

                removedEdge = [node, adjNode]

                print('edge', node, adjNode)
                if not self.isConnected(removedEdge, node):

                    if [adjNode, node] not in bridgeEdges:
                        bridgeEdges.append([node, adjNode])

        print(bridgeEdges)


if __name__ == "__main__":

    g = G(4)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)

    # g.printG()

    g.checkIfRemovingAGivenEdgeDisconnectsGraph()
