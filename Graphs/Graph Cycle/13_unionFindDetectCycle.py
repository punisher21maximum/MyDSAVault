

class Subset:

    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


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

    def find(self, node, subsets):

        if subsets[node].parent != node:
            subsets[node].parent = self.find(subsets[node].parent, subsets)
        return subsets[node].parent

    def union(self, node, adjNode, subsets):

        if subsets[node].rank == subsets[adjNode].rank:
            subsets[adjNode].parent = node
            subsets[node].rank += 1
        elif subsets[node].rank > subsets[adjNode].rank:
            subsets[adjNode].parent = node
        else:
            subsets[node].parent = adjNode

    def unionFindDetectCycleUG(self):

        subsets = []

        for node in self.graph:
            subsets.append(Subset(node, 0))

        for node in self.graph:
            adjList = self.graph[node]
            for adjNode in adjList:

                parentOfNode = self.find(node, subsets)
                parentOfAdjNode = self.find(adjNode, subsets)

                if parentOfNode == parentOfAdjNode:
                    print('cycle', node, adjNode)
                    return

                self.union(node, adjNode, subsets)


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
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(0, 2)

    # g.addEdge(0, 1)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)

    # g.printG()

    print(g.unionFindDetectCycleUG())
