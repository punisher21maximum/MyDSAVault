from collections import defaultdict


class Graph:

    def __init__(self, V):

        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):

        self.graph[u].append([v, w])

        # UG
        self.graph[v].append([u, w])

    def ifPathMoreThanLengthK(self, srcNode, K):

        visited = [False] * self.V
        visited[srcNode] = True

        if self.ifPathMoreThanLengthKHelper(srcNode, K, visited):
            print('Yes')
        else:
            print('No')

    def ifPathMoreThanLengthKHelper(self, srcNode, K, visited):

        if K <= 0:
            print('K <= 0 is True, K: ', K)
            return True

        adjList = self.graph[srcNode]
        for adjNode, weight in adjList:

            if visited[adjNode] == True:
                continue

            if weight >= K:
                print('Found, Node: ', adjNode)
                return True

            visited[adjNode] = True

            if self.ifPathMoreThanLengthKHelper(adjNode, K - weight, visited):
                return True

            visited[adjNode] = False

        return False


if __name__ == '__main__':

    g = Graph(V=9)

    #  making above shown graph
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)

    g.ifPathMoreThanLengthK(srcNode=0, K=62)
