

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

    def traverseBFS(self, src):

        visited = [False] * (max(self.graph) + 1)

        queue = [src]
        visited[src] = True

        while queue:
            nodeData = queue.pop(0)

            print(nodeData, end=' ')

            for neighbourNode in self.graph[nodeData]:
                if not visited[neighbourNode]:
                    queue.append(neighbourNode)
                    visited[neighbourNode] = True

    def traverseDFSIter(self, src):

        visited = [False] * (max(self.graph) + 1)

        stack = [src]
        visited[src] = True

        while stack:
            nodeData = stack.pop()

            print(nodeData, end=' ')

            for neighbourNode in self.graph[nodeData]:
                if not visited[neighbourNode]:
                    stack.append(neighbourNode)
                    visited[neighbourNode] = True

    def traverseDFSRecur(self, src, visited=[]):

        visited = [False] * (max(self.graph) + 1)

        visited[src] = True
        nodeData = src

        print(nodeData, end=' ')

        for neighbourNode in self.graph[nodeData]:
            if not visited[neighbourNode]:
                visited[neighbourNode] = True
                self.traverseDFSRecur(neighbourNode, visited)

    def traverseDFSRecur2Helper(self, nodeData, visited):

        visited[nodeData] = True
        print(nodeData, end=' ')

        for neighbourNode in self.graph[nodeData]:
            if not visited[neighbourNode]:
                self.traverseDFSRecur2Helper(neighbourNode, visited)

    def traverseDFSRecur2(self, src):

        visited = [False] * (max(self.graph) + 1)

        self.traverseDFSRecur2Helper(src, visited)

        for node in self.graph:
            if visited and not visited[node]:
                visited = self.traverseDFSRecur2Helper(node, visited)

    def DFSHelper(self, node, visited):
        '''
        Topological sort only for Directed Acyclic Graph
        '''

        visited.append(node)

        print(node, end=' ')

        adjacencyList = self.graph[node]
        for adjNode in adjacencyList:
            if not adjNode in visited:
                self.DFSHelper(adjNode, visited)

    def DFS(self):

        visited = []

        for node in self.graph:
            if not node in visited:
                self.DFSHelper(node, visited)


if __name__ == "__main__":

    g = G()
    # g.addEdge(0, 1)
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

    # g.traverseDFSIter(0)
    print()
    g.traverseDFSRecur(0)
    print()
    # g.traverseDFSRecur2(0)
