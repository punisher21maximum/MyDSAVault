

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

    def printAllPathsBetweenTwoNodes(self, src, destination):

        queue = [[src]]

        while queue:
            path = queue.pop(0)
            # print(path)

            lastNode = path[-1]

            if lastNode == destination:
                print(path)
                continue

            adjList = self.graph[lastNode]
            for adjNode in adjList:
                if adjNode not in path:
                    newPath = path + [adjNode]
                    queue.append(newPath)


if __name__ == "__main__":

    g = G()

    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(0, 3)
    # g.addEdge(2, 0)
    # g.addEdge(2, 1)
    # g.addEdge(1, 3)

    g.addEdge(1, 11)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 9)
    g.addEdge(11, 2)
    g.addEdge(11, 5)
    g.addEdge(2, 5)
    g.addEdge(2, 4)
    g.addEdge(2, 6)
    g.addEdge(3, 7)
    g.addEdge(5, 10)
    g.addEdge(7, 6)
    g.addEdge(4, 10)
    g.addEdge(4, 0)
    g.addEdge(6, 0)

    # g.printG()

    g.printAllPathsBetweenTwoNodes(1, 0)
