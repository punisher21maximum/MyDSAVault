

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
        # if src != dest:
        #     self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

# Code

    def find(self, node, parent):

        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]

        return parent[node]

    def union(self, node, adjNode, parent, rank):

        if rank[node] == rank[adjNode]:
            parent[adjNode] = node
            rank[node] += 1
        elif rank[node] > rank[adjNode]:
            parent[adjNode] = node
        else:
            parent[node] = adjNode

    def unionFindDetectCycleUG(self):

        parent = [-1] * len(self.graph)
        rank = [0] * len(self.graph)

        for node in self.graph:
            adjList = self.graph[node]
            for adjNode in adjList:

                parentOfNode = self.find(node, parent)
                parentOfAdjNode = self.find(adjNode, parent)

                if parentOfNode == parentOfAdjNode:
                    print('cycle', node, adjNode)
                    return

                self.union(node, adjNode, parent, rank)


if __name__ == "__main__":

    g = G()

    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(0, 2)

    # g.printG()

    print(g.unionFindDetectCycleUG())
