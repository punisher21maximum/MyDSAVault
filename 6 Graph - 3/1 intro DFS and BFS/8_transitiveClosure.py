from collections import defaultdict


class G:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):

        self.graph[src].append(dest)

        # if UG
        # self.graph[dest].append(src)

    def printG(self):

        for node in self.graph:
            adjList = self.graph[node]
            print(node, adjList)

    def DFSHelper(self, src, dest, tc):

        if src != dest:
            tc[src][dest] = 1
        elif src == dest and dest in self.graph[src]:
            tc[src][dest] = 1

        adjList = self.graph[src]
        for adjNode in adjList:
            if src == adjNode:
                tc[src][adjNode]
            else:
                self.DFSHelper(src, adjNode)

    def DFS(self):

        tc = [[0] * self.V for _ in range(self.V)]

        for node in range(self.V):
            self.DFSHelper(node, node, tc)


if __name__ == "__main__":

    g = G(11)
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

    g.printG()

    g.DFS()
