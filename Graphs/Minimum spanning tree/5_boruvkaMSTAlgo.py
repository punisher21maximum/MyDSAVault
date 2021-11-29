from collections import defaultdict


class G:

    def __init__(self, V):
        self.V = V
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, node):
        if parent[node] == node:
            return node
        return self.find(parent, parent[node])

    def union(self, parent, rank, node1, node2):

        node1root = self.find(parent, node1)
        node2root = self.find(parent, node2)

        if rank[node1root] == rank[node2root]:
            rank[node1root] += 1
            parent[node2root] = node1root
        elif rank[node1root] > rank[node2root]:
            parent[node2root] = node1root
        else:
            parent[node1root] = node2root

    def boruvkaMSTAlgo(self):
        parent, rank, cheapest = [], [], []
        numTrees, MSTweight = self.V, 0

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            cheapest.append(-1)

        while numTrees > 1:

            for edge in range(len(self.graph)):
                u, v, w = self.graph[edge]

                set1 = self.find(parent, u)
                set2 = self.find(parent, v)

                if set1 != set2:
                    if cheapest[set1] == -1 or cheapest[set1][2] > w:
                        cheapest[set1] = [u, v, w]

                    if cheapest[set2] == -1 or cheapest[set2][2] > w:
                        cheapest[set2] = [u, v, w]

            for node in range(self.V):

                if cheapest[node] != -1:
                    u, v, w = cheapest[node]

                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)

                    if set1 != set2:
                        MSTweight += w
                        self.union(parent, rank, set1, set2)
                        numTrees -= 1
                        print('edge', u, v, w)

        print('Weight: ', MSTweight)


g = G(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.boruvkaMSTAlgo()
