

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

    def printAllPathsBetweenTwoNodes(self, src, dest, numOfPaths=0, visited=[]):

        visited.append(src)

        for adjNode in self.graph[src]:
            if adjNode == dest:
                numOfPaths += 1
                print(visited+[dest], numOfPaths)

            if not adjNode in visited:
                numOfPaths = self.printAllPathsBetweenTwoNodes(
                    adjNode, dest, numOfPaths, visited)

        visited.pop()

        return numOfPaths


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

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)

    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(0, 4)
    # g.addEdge(1, 3)
    # g.addEdge(1, 4)
    # # g.addEdge(2, 1)
    # g.addEdge(2, 4)
    # g.addEdge(3, 2)

    # g.printG()

    print('numOfPaths: ', g.printAllPathsBetweenTwoNodes(0, 3))
