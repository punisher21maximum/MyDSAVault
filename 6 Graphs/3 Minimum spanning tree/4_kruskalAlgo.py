

class G:

    def __init__(self, V):
        self.V = V
        self.graph = []

    def addEdge(self, u, v, w):

        self.graph.append([u, v, w])

    def printG(self):

        for u, v, w in self.graph:
            print(u, v, w)

# Code

    def findParent(self, parent, vertex):
        if parent[vertex] == -1:
            return vertex
        else:
            return self.findParent(parent, parent[vertex])

    def union(self, parent, vertex1, vertex2):
        parent[self.findParent(parent, vertex1)] = vertex2

    def kruskalAlgo(self):
        '''
        Algo
        s1 - sort edges in non-descreasing order
        s2 - pick V-1 edges, smallest w/o creating cycle
        '''

        kruskalMST = []
        numOfEdges = 0
        weightOfMST = 0

        # s1
        edges = self.graph
        edges = sorted(edges, key=lambda edge: edge[2])

        # s2
        parent = [-1] * len(self.graph)

        for edge in edges:
            vertex1, vertex2 = edge[0], edge[1]

            parentOfV1 = self.findParent(parent, vertex1)
            parentOfV2 = self.findParent(parent, vertex2)

            if parentOfV1 != parentOfV2:
                # continue

                print(edge, vertex1, parentOfV1, vertex2, parentOfV2)

                self.union(parent, vertex1, vertex2)

                kruskalMST.append(edge)
                numOfEdges += 1
                weightOfMST += edge[2]

            if numOfEdges == self.V - 1:
                break

        print()
        return kruskalMST, numOfEdges


if __name__ == "__main__":

    graph = G(9)
    graph.addEdge(0, 1, 4)
    graph.addEdge(0, 7, 8)
    graph.addEdge(1, 2, 8)
    graph.addEdge(1, 7, 11)
    graph.addEdge(2, 3, 7)
    graph.addEdge(2, 8, 2)
    graph.addEdge(2, 5, 4)
    graph.addEdge(3, 4, 9)
    graph.addEdge(3, 5, 14)
    graph.addEdge(4, 5, 10)
    graph.addEdge(5, 6, 2)
    graph.addEdge(6, 7, 1)
    graph.addEdge(6, 8, 6)
    graph.addEdge(7, 8, 7)

    # graph = G(4)
    # graph.addEdge(0, 1, 10)
    # graph.addEdge(0, 2, 6)
    # graph.addEdge(0, 3, 5)
    # graph.addEdge(1, 3, 15)
    # graph.addEdge(2, 3, 4)

    graph.printG()

    print(graph.kruskalAlgo())
