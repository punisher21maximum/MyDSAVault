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

        if parent[node] != -1:
            return self.findParent(parent, parent[node])
        return node

    def union(self, parent, node, adjNode):

        parent[adjNode] = node

    def checkCycleUnionFind(self):
        '''
        Disjoint-set datastructure: is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets

        Union-find algo: Two funcs
        1. union: join two subsets into one | Time O(n)
        2. find: find parent(subset) of an element
        '''

        parent = [-1] * self.V

        for node in self.graph:
            adjList = self.graph[node]
            for adjNode in adjList:
                parentOfNode = self.findParent(parent, node)
                parentOfAdjNode = self.findParent(parent, adjNode)

                if parentOfNode == parentOfAdjNode:
                    print('Cycle')
                    return

                self.union(parent, parentOfNode, parentOfAdjNode)

        print('No Cycle')
        print(parent)


if __name__ == "__main__":

    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 1)

    g.printG()

    g.checkCycleUnionFind()
