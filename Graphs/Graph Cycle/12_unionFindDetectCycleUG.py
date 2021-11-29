

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

    def findParent(self, parent, node):
        if parent[node] == -1:
            return node
        else:
            return self.findParent(parent, parent[node])

    def union(self, parent, node, adjNode):
        parent[node] = adjNode

    def unionFindDetectCycleUG(self):
        '''
        Algo name: DisjointSet/UnionFind
        disjoint data structure -  a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets
        find - finds to which subset element belongs
        union - join two subsets into one

        algo:
        for each edge check if both vertex belong to different set
        '''
        parent = [-1] * len(self.graph)

        for node in self.graph:
            adjacencyList = self.graph[node]
            # edge: node----adjNodes
            for adjNode in adjacencyList:
                parentOfNode = self.findParent(parent, node)
                parentOfAdjNode = self.findParent(parent, adjNode)

                if parentOfNode == parentOfAdjNode:
                    print('cycle', node, adjNode)
                    return True

                self.union(parent, node, adjNode)

        return False


if __name__ == "__main__":

    g = G()
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 3)
    # g.addEdge(1, 4)
    # g.addEdge(2, 5)
    # g.addEdge(2, 6)
    # g.addEdge(3, 7)
    # g.addEdge(3, 8)
    # g.addEdge(4, 9)
    # g.addEdge(4, 10)

    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(2, 3)
    # g.addEdge(3, 3)

    # # g.addEdge(0, 0)
    # g.addEdge(0, 1)
    # g.addEdge(1, 2)
    # g.addEdge(2, 3)

    # g.addEdge(0, 1)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)

    # g.printG()

    print(g.unionFindDetectCycleUG())
