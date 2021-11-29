

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

# Bad complexity

    def findMotherNodeHelper(self, node, cache):

        reachableNodes = self.graph[node] + [node]

        for adjNode in self.graph[node]:
            if adjNode in cache:
                reachableNodes += cache[adjNode]
            else:
                reachableNodes += self.findMotherNodeHelper(
                    adjNode, cache)

        cache[node] = reachableNodes

        return reachableNodes

    def findMotherNode(self):

        numOfVertices = len(self.graph)
        cache = {}
        reachableNodes = []

        for node in [4, 9, 10, 3, 7, 8, 2, 1, 0]:  # self.graph:

            reachableNodes = []

            if node in cache:
                reachableNodes += cache[node]
            else:
                reachableNodes += self.findMotherNodeHelper(
                    node, cache)

            reachableNodes = list(set(reachableNodes))

            if numOfVertices == len(reachableNodes):
                print('Mother node: ', node)
                break

            print(node, reachableNodes)


if __name__ == "__main__":

    g = G()
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

    # graph.printG()

    g.findMotherNode()
