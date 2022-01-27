

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
        if src != dest:
            self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

# Code

    def printAllPathsBetweenTwoNodes(self, node, parent=None, visited=[]):

        visited.append(node)

        adjacencyList = self.graph[node]

        for adjNode in adjacencyList:
            if adjNode == parent or adjNode == node:
                continue

            if adjNode in visited:
                print('cycle', visited+[adjNode])
                return True

            if not adjNode in visited:
                return self.printAllPathsBetweenTwoNodes(
                    adjNode, node, visited)

        visited.pop()

        return False


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

    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(0, 3)
    g.addEdge(3, 4)

    # g.addEdge(0, 0)
    # g.addEdge(0, 1)
    # g.addEdge(1, 2)
    # g.addEdge(2, 3)

    g.printG()

    print(g.printAllPathsBetweenTwoNodes(0))
