

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

    def countNumOfNodesAtAGivenLevelUsingBFS(self, givenLevel, src=0):

        queue = []
        visited = [False] * len(self.graph)

        queue = [src]
        visited[src] = True
        level = -1

        while queue:
            levelLength = len(queue)
            level += 1
            if level == givenLevel:
                return len(queue)

            for i in range(levelLength):
                node = queue.pop(0)

                adjacencyList = self.graph[node]
                for adjNode in adjacencyList:
                    if not visited[adjNode]:
                        visited[adjNode] = True
                        queue.append(adjNode)


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
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)

    # g.printG()

    # node = 2
    # print(g.getReachableNodesFromANode(node, reachableNodes=[node]))

    print(g.countNumOfNodesAtAGivenLevelUsingBFS(2))
