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

    def topologicalSortHelper(self, node, visited, stack):

        visited[node] = True

        adjList = self.graph[node]
        for adjNode in adjList:
            if not visited[adjNode]:
                self.topologicalSortHelper(adjNode, visited, stack)

        stack.append(node)

    def topologicalSort(self):
        '''
        topological order: linear ordering of vertices such that for every directed edge u v, 
        vertex u comes before v in the ordering

        Approach:
        in stack we store, nodes in low to high degree from bottom to top 
        we first put the node with lowest degree in stack

        '''
        visited = [False] * self.V
        stack = []

        for node in [3, 4, 5, 0, 1, 2]:  # range(self.V):
            if not visited[node]:
                self.topologicalSortHelper(node, visited, stack)

        print(stack[::-1])


if __name__ == "__main__":

    g = G(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    g.topologicalSort()
