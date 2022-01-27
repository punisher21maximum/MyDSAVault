from collections import defaultdict


class Graph:

    def __init__(self, V):

        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)

        # UG
        # self.graph[v].append([u, w])

    def printAllPathFromGivenSrcToDest(self, srcNode, destNode):

        visited = [False] * self.V
        visited[srcNode] = True
        path = [srcNode]

        self.printAllPathFromGivenSrcToDestHelper(
            srcNode, destNode, visited, path)

    def printAllPathFromGivenSrcToDestHelper(self, srcNode, destNode, visited, path):

        adjList = self.graph[srcNode]
        for adjNode in adjList:

            if visited[adjNode] == True:
                continue

            visited[adjNode] = True
            path.append(adjNode)

            if adjNode == destNode:
                print('Path: ', path)

            self.printAllPathFromGivenSrcToDestHelper(
                adjNode, destNode, visited, path)

            visited[adjNode] = False
            path.pop()


if __name__ == '__main__':

    g = Graph(4)

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)

    g.printAllPathFromGivenSrcToDest(srcNode=2, destNode=3)
