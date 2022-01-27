from collections import defaultdict


class G:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):

        self.graph[src].append(dest)

        # for undirected graph
        self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

    def countCyclesOfLengthNUCGHelper(self, visited, N, startNode,
                                      currNode, numCycles):
        """
        DFS
        """
        visited[currNode] = True

        if N == 0:
            visited[currNode] = False

            if startNode == currNode:
                numCycles += 1

            return numCycles

        adjList = self.graph[currNode]
        for adjNode in adjList:
            if not visited[adjNode]:
                numCycles = self.countCyclesOfLengthNUCGHelper(visited, N - 1, startNode,
                                                               adjNode, numCycles)
        visited[currNode] = False
        return numCycles

    def countCyclesOfLengthNUCG(self, N):
        '''
        Approach: count cycles of length N
        - start from each vertex one by one 
        - explore all paths of length N
        - after length (N-1), check if Nth node same as start node 


        Every possible path of length (n-1) can be searched using only V – (n – 1) vertices (where V is the total number of vertices). 
        For above example, all the cycles of length 4 can be searched using only 5-(4-1) = 2 vertices. The reason behind this is quite simple, because we search for all possible path of length (n-1) = 3 using these 2 vertices which include the remaining 3 vertices. So, these 2 vertices cover the cycles of remaining 3 vertices as well, and using only 3 vertices we can’t form a cycle of length 4 anyways. 
        '''
        visited = [False] * self.V

        numCycles = 0
        for node in range(self.V - (N - 1)):
            numCycles = self.countCyclesOfLengthNUCGHelper(
                visited, N-1, node, currNode=node, numCycles=0)

            visited[node] = True

        print(numCycles//2)


if __name__ == "__main__":

    g = G(5)
    g.addEdge(0, 1)
    g.addEdge(0, 3)
    # g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(1, 4)
    # g.addEdge(2, 1)
    g.addEdge(2, 3)
    # g.addEdge(3, 0)
    # g.addEdge(3, 2)
    g.addEdge(3, 4)
    # g.addEdge(4, 1)
    # g.addEdge(4, 3)

    g.printG()

    g.countCyclesOfLengthNUCG(4)
