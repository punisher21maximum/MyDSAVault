'''
1. create G
2. find which is the first letter to be chosen based on second or third letter
'''


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

        self.V = len(self.graph)

    def printG(self):

        for node in self.graph:
            print(node, self.graph[node])

    def petersonProblem(self, walk, currNode):

        for i in range(len(walk)):
            nextStep = walk[i]
            nextNodeInOuter = ord(nextStep) - ord('A')
            nextNodeInInner = ord(nextStep) - ord('A') + 5

            adjList = self.graph[currNode]
            if nextNodeInOuter in adjList:
                currNode = nextNodeInOuter
            elif nextNodeInInner in adjList:
                currNode = nextNodeInInner
            else:
                print('Not Possible')
                return False

            print(currNode, end=' ')

        return True


if __name__ == "__main__":

    g = G()

    # A - A
    g.addEdge(0, 5)
    g.addEdge(1, 6)
    g.addEdge(2, 7)
    g.addEdge(3, 8)
    g.addEdge(4, 9)
    # outer
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 0)
    # inner
    g.addEdge(5, 7)
    g.addEdge(6, 8)
    g.addEdge(7, 9)
    g.addEdge(8, 5)
    g.addEdge(9, 6)

    g.printG()

    walk = 'ABBECCD'
    startNodeInOuter = ord(walk[0]) - ord('A')
    startNodeInInner = ord(walk[0]) - ord('A') + 5
    nodeOrder = []

    if (g.petersonProblem(walk, startNodeInOuter) or
            g.petersonProblem(walk, startNodeInInner)):
        print('Possible')
    else:
        print('Impossible')
