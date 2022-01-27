from collections import defaultdict


class G:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(set)
        '''
        when self.V = 4, nodes -> [0, 3] 
        pseudoNode can be a new node, diff from existing ones 
        so psedoCode can be maxNode+1 = 3 + 1 = self.V
        '''
        self.pseudoNode = 999

    def addEdge(self, src, dest, weight):

        if weight % 2 == 0:  # even
            self.addEdge(src, self.pseudoNode, 1)
            self.addEdge(self.pseudoNode, dest, 1)
        else:
            self.graph[src].add(dest)

            # for undirected graph
            self.graph[dest].add(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

    def checkIfCycleWithOddWeightSumUG(self, src=0):
        '''
        Thoery:
        Bi-partite Graph:
        All vertices of G, divided into two sets.
        Vertices of the same set are not connected.

        - Bi-partite graph : Does not contain cycle of odd length 
        - If graph has no odd length cycle : Bi-partite graph   

        Approach:
        To check if cycle of odd length 
        Check if Bi-partite Graph
            if yes: No odd length cycle 
            if no: Maybe an even length cycle

        Algo: 
        Traverse BFS 
        if adjNode has no color, assign diff color from currNode & push to queue 
        if adjNode has color, check if currNode and adjNode has same color
            if yes, odd length cycle
        '''
        colorSet = [None] * self.V
        colorSet[src] = 'Red'

        queue = [src]
        while queue:
            node = queue.pop()

            adjList = self.graph[node]
            for adjNode in adjList:
                if not colorSet[node]:
                    colorSet[adjNode] = 'Red' if colorSet[node] == 'Blue' else 'Red'
                    queue.append(adjNode)
                elif colorSet[node] == colorSet[adjNode]:
                    print('Not Bi-partite | Has odd length Cycle')
                    return True
        print('Bi-partite | No odd length cycle')
        return False


if __name__ == "__main__":

    g = G(4)
    g.addEdge(1, 2, 12)
    g.addEdge(2, 3, 1)
    g.addEdge(4, 3, 1)
    g.addEdge(4, 1, 20)

    g.printG()

    res = g.checkIfCycleWithOddWeightSumUG(0)
    print(res)
