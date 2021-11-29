

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

    def findMotherNodeHelper(self, node, visited):

        visited[node] = True

        for adjNode in self.graph[node]:
            if not visited[adjNode]:
                self.findMotherNodeHelper(adjNode, visited)

    def findMotherNode(self):

        visited = [False] * len(self.graph)
        potentialMotherVertex = 0

        for nodeData in [2, 3, 4, 0]:  # self.graph
            if not visited[nodeData]:
                self.findMotherNodeHelper(nodeData, visited)
                potentialMotherVertex = nodeData

        visited = [False] * len(self.graph)
        self.findMotherNodeHelper(potentialMotherVertex, visited)

        if False in visited:
            return -1
        motherVertex = potentialMotherVertex
        return motherVertex


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

    # g.printG()

    print(g.findMotherNode())
