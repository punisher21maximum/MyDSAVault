

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
        # if src != dest:
        #     self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])


# Code


    def detectCycleDirectedUsingColorHelper(self, node, color):
        ''' color
        white: not yet traversed
        grey: undergoing traversal
        black: traversal done
        '''

        color[node] = 'grey'
        print('node', node)
        adjacencyList = self.graph[node]
        for adjNode in adjacencyList:
            print(color[node], node, adjNode, adjacencyList)
            if color[adjNode] == 'black':
                print('black', node, adjNode)
                continue

            if color[adjNode] == 'grey':
                print('cycle|grey', node, adjNode)
                return True

            if color[adjNode] == 'white':
                return self.detectCycleDirectedUsingColorHelper(
                    adjNode, color)

        color[node] = 'black'

        return False

    def detectCycleDirectedUsingColor(self):

        color = {}
        for node in self.graph:
            color[node] = 'white'

        return self.detectCycleDirectedUsingColorHelper(0, color)


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

    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(2, 3)
    # g.addEdge(3, 3)

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 4)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 4)
    g.addEdge(3, 2)
    g.addEdge(4, 5)
    g.addEdge(4, 6)

    g.printG()

    print(g.detectCycleDirectedUsingColor())
