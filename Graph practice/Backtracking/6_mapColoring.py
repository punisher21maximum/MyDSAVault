from collections import defaultdict


class G:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):

        self.graph[src].append(dest)

        # for undirected graph
        self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

    def mapColoring(self, M):
        '''
        Find if UG can be colored with M colors.
        If adj nodes should have diff colors.
        '''
        colors = [i for i in range(1, M+1)]
        colorMap = dict()

        for node in self.graph:
            for color in colors:
                adjList = self.graph[node]

                isColorInAdj = False
                for adjNode in adjList:
                    if adjNode in colorMap and colorMap[adjNode] == color:
                        isColorInAdj = True
                        break

                if not isColorInAdj:
                    colorMap[node] = color
                    break


if __name__ == "__main__":

    g = G(11)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(1, 2)
    g.addEdge(2, 3)

    # graph.printG()

    g.mapColoring(3)
