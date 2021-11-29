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

    def findParent(self, subsets, node):

        if subsets[node][0] != node:
            subsets[node][0] = self.findParent(subsets, subsets[node][0])
        return subsets[node][0]

    def union(self, subsets, node, adjNode):
        '''
        rank: subsets[node][1]
        '''
        if subsets[node][1] > subsets[adjNode][1]:
            subsets[adjNode][0] = node
        elif subsets[node][1] < subsets[adjNode][0]:
            subsets[node][0] = adjNode
        else:
            subsets[node][1] += 1  # inc rank
            subsets[adjNode][0] = node  # update parent

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

        subsets = []

        for node in range(self.V):
            subsets.append([node, 0])  # [parent, rank]

        for node in self.graph:
            adjList = self.graph[node]
            for adjNode in adjList:
                parentOfNode = self.findParent(subsets, node)
                parentOfAdjNode = self.findParent(subsets, adjNode)
                print('1->', node, parentOfNode, adjNode, parentOfAdjNode)

                if parentOfNode == parentOfAdjNode:
                    print('Cycle')
                    return

                self.union(subsets, node, adjNode)
                print(subsets)

        print('No Cycle')
        print(subsets)


if __name__ == "__main__":

    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 1)

    g.printG()

    g.checkCycleUnionFind()
