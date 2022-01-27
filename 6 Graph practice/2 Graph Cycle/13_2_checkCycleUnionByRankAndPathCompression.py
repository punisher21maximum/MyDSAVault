from collections import defaultdict


class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):

        self.graph[src].append(dest)

        # for undirected graph
        # self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

    def findParent(self, parent, node):

        if parent[node] != node:
            parent[node] = self.findParent(parent, parent[node])
        return parent[node]

    def union(self, parent, rank, node, adjNode):

        if rank[node] > rank[adjNode]:
            parent[adjNode] = node
        elif rank[node] < rank[adjNode]:
            parent[node] = adjNode
        else:
            rank[node] += 1
            parent[adjNode] = node

    def checkCycleUnionFind(self):
        '''
        Disjoint-set datastructure: is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets

        Union-find algo | Optimised: Two funcs
        1. union: 
            simple union func is naive as it can lead to skewed tree | Time O(n) 

            optmised | Time O(logN) - attach smaller depth tree to deeper one 
            depth is stored as ranks, (fact: rank not always equal to height)

        2. find: find parent(subset) of an element
            Path compression | Time O(logN) - Say, we find() parent parentX of node nodeX 
            so now we assign parentX, directly to nodeX.
        '''

        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        for node in self.graph:
            adjList = self.graph[node]
            for adjNode in adjList:
                parentOfNode = self.findParent(parent, node)
                parentOfAdjNode = self.findParent(parent, adjNode)

                if parentOfNode == parentOfAdjNode:
                    print('Cycle')
                    return

                self.union(parent, rank, node, adjNode)

        print('No Cycle')
        print(parent)
        print(rank)


if __name__ == "__main__":

    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 1)

    g.printG()

    g.checkCycleUnionFind()
