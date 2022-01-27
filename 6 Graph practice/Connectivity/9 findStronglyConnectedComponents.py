from collections import defaultdict


class G:

    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self, src, dest):

        self.graph[src].append(dest)

        # for undirected graph
        # self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

    def getTranspose(self):
        transposeG = G(self.V)

        for node in self.graph:
            adjList = self.graph[node]
            for adjNode in adjList:
                transposeG.addEdge(adjNode, node)

        return transposeG

    def fillOrder(self, node, visited, stack):

        visited[node] = True

        adjList = self.graph[node]
        for adjNode in adjList:
            if not visited[adjNode]:
                self.fillOrder(adjNode, visited, stack)

        stack = stack.append(node)

    def DFSUtil(self, node, visited):

        visited[node] = True
        print(node, end=" ")

        adjList = self.graph[node]
        for adjNode in adjList:
            if not visited[adjNode]:
                self.DFSUtil(adjNode, visited)

    def findAllStronglyConnectedComponents(self):
        '''
        Strongly Connected Components SSC:
        SSC is sub-graph in graph, in which
        each node can reach every other node

        Approach:
        s1: 
        '''
        stack = []  # to keep order of nodes

        visited = [False] * self.V

        # fill nodes in stack as per finishing time
        for node in range(self.V):
            if not visited[node]:
                self.fillOrder(node, visited, stack)

        transposeG = self.getTranspose()

        visited = [False] * transposeG.V

        while stack:
            node = stack.pop()
            if not visited[node]:
                transposeG.DFSUtil(node, visited)
                print()


if __name__ == "__main__":

    g = G(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(3, 4)

    # graph.printG()

    g.findAllStronglyConnectedComponents()
