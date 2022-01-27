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

        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(self, parent, rank, node, adjNode):
        '''
        rank: rank[node][1]
        '''
        if rank[node] >= rank[adjNode]:
            parent[adjNode] = parent[node]  # assign parent instead of node
            rank[node] += rank[adjNode]
        else:
            parent[node] = parent[adjNode]  # assign parent instead of node
            rank[adjNode] += rank[node]

    def checkCycleUnionFind(self):
        '''
        arr: similar to parent
        size: similar to rank

        Union-find algo | Optimised: Two funcs
        1. union: 
            optmised | Time O(logN) - 1. by rank 2. assign parent 

        2. find: find parent(subset) of an element
            Path compression | Time O(1) for repeated calls 
        '''

        parent = [i for i in range(self.V)]
        rank = [1] * self.V

        for node in self.graph:
            adjList = self.graph[node]
            for adjNode in adjList:
                parentOfNode = self.findParent(parent, node)
                parentOfAdjNode = self.findParent(parent, adjNode)
                print(parent)
                if parentOfNode == parentOfAdjNode:
                    print('Cycle')
                    return

                self.union(parent, rank, node, adjNode)
                # print(parent)
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
