

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

    def checkIfBipartite(self, src, nodeColor={}, color='red'):
        '''
        Algorithm:
        color the root node with 'red'
        then color the adjNodes with 'blue'
        and thier adjNodes with 'red', and so on
        if a node and adjNode has same color -> Non Bipartite
        '''

        queue = [src]

        while queue:
            node = queue.pop(0)

            if node in nodeColor:
                continue

            nodeColor[node] = color
            color = 'blue' if color == 'red' else 'red'

            adjList = self.graph[node]
            for adjNode in adjList:
                if adjNode not in nodeColor:
                    self.checkIfBipartite(adjNode, nodeColor, color)
                if nodeColor[node] == nodeColor[adjNode]:
                    return ('False', node, adjNode, nodeColor)

        return nodeColor


if __name__ == '__main__':

    g = G()

    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(5, 0)

    g.printG()

    print(g.checkIfBipartite(0))
