

class G:

    def __init__(self):
        self.graph = dict()

    def addEdge(self, src, dest):

        if src not in self.graph:
            self.graph[src] = []
        if dest not in self.graph:
            self.graph[dest] = []

        self.graph[src].append(dest)

        # for undirected graph
        # self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

# Code

    def getReachableNodesFromANode(self, node, reachableNodes):

        adjacencyList = self.graph[node]

        for adjNode in adjacencyList:
            if adjNode not in reachableNodes:
                reachableNodes.append(adjNode)
                self.getReachableNodesFromANode(adjNode, reachableNodes)

        return reachableNodes

    def isTrasitiveClosure(self):

        V = len(self.graph)
        transitiveClosure = []

        for node in self.graph:
            reachableNodes = [node]
            reachableNodes = self.getReachableNodesFromANode(
                node, reachableNodes)
            transitiveClosure.append(reachableNodes)

            if not len(reachableNodes) == V:
                return False, print(transitiveClosure)

        return True, print(transitiveClosure)


if __name__ == "__main__":

    g = G()
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 3)
    # g.addEdge(1, 4)
    # g.addEdge(2, 5)
    # g.addEdge(2, 6)
    # g.addEdge(3, 7)
    # g.addEdge(3, 8)
    # g.addEdge(4, 9)
    # g.addEdge(4, 10)

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)

    # g.printG()

    # node = 2
    # print(g.getReachableNodesFromANode(node, reachableNodes=[node]))

    print(g.isTrasitiveClosure())
