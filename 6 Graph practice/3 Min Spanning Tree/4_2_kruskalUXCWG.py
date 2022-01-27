
from collections import defaultdict


class Edge:
    def __init__(self, u, v, wt):
        self.u = u
        self.v = v
        self.wt = wt


class G:

    def __init__(self, V):
        self.V = V
        self.graph = []

    def addEdge(self, u, v, wt):

        newEdge = Edge(u, v, wt)
        self.graph.append(newEdge)

        # for undirected graph
        # self.graph[dest].append(src)

    def printG(self):

        for edge in self.graph:
            print(':', edge.u, edge.v, edge.wt)

    def find(self, parent, node):
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])
        return parent[node]

    def union(self, parent, rank, node, adjNode):

        if rank[node] > rank[adjNode]:
            parent[adjNode] = node
        elif rank[node] < rank[adjNode]:
            parent[node] = adjNode
        else:
            rank[node] += 1
            parent[adjNode] = node

    def kruskalMST(self):
        """
        Approach:
        1. Sort of edges by inc order of weight 
        2. one by one select an edge 
        3. check if selected edge will form cycle with current MST
            if no - add to MST
            else - dont 
        4. continue until we have V - 1 edges
        """
        minSpanningTree = []
        # s1: sort the edges
        self.graph = sorted(self.graph,
                            key=lambda edge: edge.wt)

        parent, rank = [], []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # s2:
        for edge in self.graph:
            print(edge.u, edge.v)
            if len(minSpanningTree) == self.V - 1:
                break

            parentOfU = self.find(parent, edge.u)
            parentOfV = self.find(parent, edge.v)

            if parentOfU != parentOfV:
                minSpanningTree.append(edge)
                self.union(parent, rank, parentOfU, parentOfV)

        for edge in minSpanningTree:
            print('>', edge.u, edge.v, edge.wt)


if __name__ == "__main__":

    g = G(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    # g.printG()

    # Function call
    g.kruskalMST()
