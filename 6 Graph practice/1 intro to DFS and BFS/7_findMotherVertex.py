

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
        # self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

    def DFSUtil(self, node, visited):

        visited[node] = True

        adjList = self.graph[node]
        for adjNode in adjList:
            if not visited[adjNode]:
                self.DFSUtil(adjNode, visited)

    def findMotherVertex(self):  # Time O(V + E)
        '''
        Case 1: Undirected connected graph UCG 
        All vertices are mother vertex 
        Case 2: Undirected/Directed disconnected graph UDG/DDG 
        None is mother vertex 
        Case 3: Directed connected graph DCG 
        Can't say directly, will solve this

        DCG:
        Approach 1: O(V(E+V))
        Each vertex is tested if its a mother vertex. 
        For test, we do BFS/DFS, if all nodes visited,
        then its a mother vertex.

        Approach 2:
        find the vertex V that finishes last in DFS
        V can be one (of the) mother vertices
        check if all nodes reachable from V
        '''
        visited = [False] * self.V

        potentialMotherNode = None

        for node in self.graph:
            if not visited[node]:
                self.DFSUtil(node, visited)
                potentialMotherNode = node

        visited = [False] * self.V
        self.DFSUtil(potentialMotherNode, visited)
        # if mother vertex, all nodes must be visited
        for node in self.graph:
            if not visited[node]:
                return False

        return True


if __name__ == "__main__":

    g = G()
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

    g.traverseDFS(0)
