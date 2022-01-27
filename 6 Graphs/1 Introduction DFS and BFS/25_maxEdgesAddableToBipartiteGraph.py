

class G:

    def __init__(self):
        self.graph = dict()

    def addEdge(self, u, v):

        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def printG(self):

        for node in self.graph:
            print(node, self.graph[node])

    def printUAndV(self, nodeColour):

        print('Red', end=': ')
        for node in nodeColour:
            if nodeColour[node] == 'Red':
                print(node, end=' ')

        print('\nBlue', end=': ')
        for node in nodeColour:
            if nodeColour[node] == 'Blue':
                print(node, end=' ')

    def checkIfBipartiteHelper(self, src, nodeColour, colour):
        '''
        Algorithm:
        colour the root node with 'red'
        then colour the adjNodes with 'blue'
        and thier adjNodes with 'red', and so on
        if a node and adjNode has same colour -> Non Bipartite
        '''

        queue = [src]

        while queue:
            node = queue.pop(0)
            print(node)
            if node in nodeColour:
                continue

            nodeColour[node] = colour
            colour = 'blue' if colour == 'red' else 'red'

            adjList = self.graph[node]
            for adjNode in adjList:
                if adjNode not in nodeColour:
                    self.checkIfBipartiteHelper(adjNode, nodeColour, colour)
                if nodeColour[node] == nodeColour[adjNode]:
                    return ('False', node, adjNode, nodeColour)

        return nodeColour, colour

    def checkIfBipartite(self, src):

        nodeColour = dict()
        colour = 'red'

        for node in self.graph:
            if node not in nodeColour:
                nodeColour, colour = self.checkIfBipartiteHelper(
                    node, nodeColour, colour)

        self.printUAndV(nodeColour)
        print(nodeColour)
        self.getMaxEdgesAddableToBipartiteGraph(nodeColour)

    def getMaxEdgesAddableToBipartiteGraph(self, nodeColour):

        numOfEdgesFromUToV = 0
        numOfNodesInU = 0
        numOfNodesInV = 0
        maxEdgesPossibleFromUToV = 0

        for node in nodeColour:
            if nodeColour[node] == 'red':
                numOfEdgesFromUToV += 1

                numOfNodesInU += 1
            else:
                numOfNodesInV += 1

        maxEdgesPossibleFromUToV = numOfNodesInU * numOfNodesInV

        maxEdgesAddableToBipartiteGraph = (
            maxEdgesPossibleFromUToV - numOfEdgesFromUToV)

        print(numOfNodesInU, numOfNodesInV,
              numOfEdgesFromUToV, maxEdgesPossibleFromUToV, maxEdgesAddableToBipartiteGraph)


if __name__ == '__main__':

    g = G()

    # g.addEdge(0, 1)
    # g.addEdge(1, 2)
    # g.addEdge(2, 3)
    # g.addEdge(3, 4)
    # g.addEdge(4, 5)
    # g.addEdge(5, 0)

    g.addEdge(0, 5)
    g.addEdge(0, 7)
    g.addEdge(1, 5)
    g.addEdge(1, 8)
    g.addEdge(2, 6)
    g.addEdge(3, 6)
    g.addEdge(4, 7)

    g.printG()

    nodeColour = g.checkIfBipartite(0)
