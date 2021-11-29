
class adjacentNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:

    def __init__(self, numOfVetices):
        self.numOfVertices = numOfVetices
        self.graph = [None] * self.numOfVertices

    def addEdge(self, src, dest):

        # add src -> dest
        node = adjacentNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # add dest -> src
        node = adjacentNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def printGraph(self):

        for i in range(self.numOfVertices):
            print(i, ':', end='')

            tempNode = self.graph[i]
            while tempNode:
                print(' ->', tempNode.data, end='')
                tempNode = tempNode.next
            print()


if __name__ == "__main__":
    V = 6
    graph = Graph(V)
    graph.addEdge(5, 1)
    graph.addEdge(5, 4)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)

    graph.printGraph()
