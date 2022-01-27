

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

    def traverseDFS(self, srcNode):
        '''
        Iterative: with stack
        '''

        visited = [False] * len(self.graph)

        stack = [srcNode]
        while stack:
            node = stack.pop()

            visited[node] = True
            print(node, end=' ')

            adjList = self.graph[node]
            for i in reversed(range(len(adjList))):
                adjNode = adjList[i]
                if not visited[adjNode]:
                    stack.append(adjNode)

    def traverseDFSTwoHelper(self, node, visited):
        '''
        Recursive: with stack
        '''
        print(node, end=' ')
        visited[node] = True

        adjList = self.graph[node]
        for i in range(len(adjList)):
            adjNode = adjList[i]

            if not visited[adjNode]:
                self.traverseDFSTwoHelper(adjNode, visited)

    def traverseDFSTwo(self, srcNode):

        visited = [False] * len(self.graph)
        self.traverseDFSTwoHelper(srcNode, visited)


if __name__ == "__main__":

    g = G()
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

    # graph.printG()

    g.traverseDFSTwo(0)
