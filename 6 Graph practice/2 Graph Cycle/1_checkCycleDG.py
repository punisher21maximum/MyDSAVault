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

    def isCycleHelper(self, node, visited, recursionStack):

        visited[node] = True
        recursionStack[node] = True

        adjList = self.graph[node]
        for adjNode in adjList:
            if not visited[adjNode]:
                self.isCycleHelper(adjNode, visited, recursionStack)
            elif recursionStack[adjNode] == True:
                return True  # cycle

        k = recursionStack[:]
        for i in range(len(recursionStack)):
            if recursionStack[i]:
                k[i] = i
            else:
                k[i] = ' '
        print(k)

        recursionStack[node] = False
        return False

    def isCycleDG(self):
        '''
        visited: all visited vertex till now
        recursionStack: curr path
        '''
        visited = [False] * self.V
        recursionStack = [False] * self.V

        for node in range(self.V):
            if not visited[node]:
                if self.isCycleHelper(node, visited, recursionStack):
                    return True

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

    g.isCycleDG()
