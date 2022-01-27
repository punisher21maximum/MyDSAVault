

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
        self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

# Code

    def countNodesFromMarkedNodesWithinKDist(self, markedNodes, k):

        hashTable = {}
        count = 0

        for i in range(len(markedNodes)):
            markedNode = markedNodes[i]

            queue = [markedNode]
            for dist in range(k-1):
                if not queue:
                    break

                node = queue.pop()

                adjList = self.graph[node]
                for adjNode in adjList:
                    if adjNode not in hashTable:
                        hashTable[adjNode] = True
                        count += 1

        print(hashTable, count)


if __name__ == "__main__":

    g = G()

    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(0, 3)
    # g.addEdge(2, 0)
    # g.addEdge(2, 1)
    # g.addEdge(1, 3)

    # g.addEdge(1, 11)
    # g.addEdge(1, 2)
    # g.addEdge(1, 3)
    # g.addEdge(1, 9)
    # g.addEdge(11, 2)
    # g.addEdge(11, 5)
    # g.addEdge(2, 5)
    # g.addEdge(2, 4)
    # g.addEdge(2, 6)
    # g.addEdge(3, 7)
    # g.addEdge(5, 10)
    # g.addEdge(7, 6)
    # g.addEdge(4, 10)
    # g.addEdge(4, 0)
    # g.addEdge(6, 0)

    g.addEdge(1, 0)
    g.addEdge(0, 8)
    g.addEdge(0, 3)
    g.addEdge(2, 3)
    g.addEdge(3, 6)
    g.addEdge(3, 7)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(9, 5)

    # g.printG()

    g.countNodesFromMarkedNodesWithinKDist([1, 2, 3], 3)
