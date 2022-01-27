from collections import defaultdict


class G:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):

        self.graph[src].append(dest)

        # for undirected graph
        # self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

    def isCycleDGUsingColorHelper(self, node, visitColor):

        visitColor[node] = 'Gray'

        adjList = self.graph[node]
        for adjNode in adjList:
            if visitColor[adjNode] == 'White':
                self.isCycleDGUsingColorHelper(adjNode, visitColor)
            elif visitColor[adjNode] == 'Gray':
                return True  # cycle

        visitColor[node] = 'Black'
        return False

    def isCycleDGUsingColor(self):
        '''
        White: Not visited
        Gray: Being visited 
        Black: visited

        Using DFS
        '''
        visitColor = ['White'] * self.V

        for node in range(self.V):
            if visitColor[node] == 'White':
                if self.isCycleDGUsingColorHelper(node, visitColor):
                    return True

        return False


if __name__ == "__main__":

    g = G(11)
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

    g.isCycleDGUsingColor()
