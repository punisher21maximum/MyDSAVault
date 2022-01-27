from collections import defaultdict


class G:

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

    def checkIfCycleOfOddLengthGraph(self, src=0):
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
            if no: Maybe an odd length cycle

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

    g = G(11)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(2, 6)
    g.addEdge(3, 7)
    g.addEdge(3, 8)
    g.addEdge(4, 9)
    g.addEdge(4, 10)

    # graph.printG()

    res = g.checkIfCycleOfOddLengthGraph(0)
    print(res)
