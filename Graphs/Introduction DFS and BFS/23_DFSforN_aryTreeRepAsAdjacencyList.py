

class NAryTree:

    def __init__(self):
        self.tree = dict()

    def addEdge(self, u, v):

        if u not in self.tree:
            self.tree[u] = []
        if v not in self.tree:
            self.tree[v] = []

        self.tree[u].append(v)
        self.tree[v].append(u)

        self.V = len(self.tree)

    def printNAryTree(self):

        for node in self.tree:
            adjacencyList = self.tree[node]
            print(node, adjacencyList)

    def DFSForNAryTreeRepAsAdjacencyList(self, src, visited=[]):
        '''
        using "visited"
        '''
        stack = [src]

        while stack:
            node = stack.pop()

            if visited[node]:
                continue

            visited[node] = True
            print(node, end=' ')

            adjancencyList = self.tree[node]
            for adjNode in adjancencyList:
                self.DFSForNAryTreeRepAsAdjacencyList(adjNode, visited)

    def DFSForNAryTreeRepAsAdjacencyList_2(self, src, parentOfNode):
        '''
        using "parent"
        '''
        stack = [src]

        while stack:
            node = stack.pop()

            print(node, end=' ')

            adjancencyList = self.tree[node]
            for adjNode in adjancencyList:
                if adjNode != parentOfNode:
                    self.DFSForNAryTreeRepAsAdjacencyList_2(adjNode, node)


if __name__ == "__main__":

    t = NAryTree()
    t.addEdge(0, 1)
    t.addEdge(0, 2)
    t.addEdge(1, 3)
    t.addEdge(2, 4)

    t.printNAryTree()

    visited = [False] * t.V
    t.DFSForNAryTreeRepAsAdjacencyList(0, visited)

    # parent of 0 is -1
    print()
    t.DFSForNAryTreeRepAsAdjacencyList_2(0, -1)
