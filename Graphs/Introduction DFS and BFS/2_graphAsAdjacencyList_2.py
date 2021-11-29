
class adjacentNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:

    def __init__(self):
        self.graph = dict()

    def addEdge(self, src, dest):

        if src not in self.graph:
            self.graph[src] = None

        if dest not in self.graph:
            self.graph[dest] = None

        # add src -> dest
        node = adjacentNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # add dest -> src || for undirected graphs
        node = adjacentNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def printGraph(self):

        for i in self.graph:
            print(i, ':', end='')

            tempNode = self.graph[i]
            while tempNode:
                print(' ->', tempNode.data, end='')
                tempNode = tempNode.next
            print()


if __name__ == "__main__":

    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(0, 4)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)

    graph.printGraph()
