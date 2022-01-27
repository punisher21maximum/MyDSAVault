

class G:

    def __init__(self, V):
        self.graph = dict()
        self.V = V

    def addEdge(self, src, dest, weight):

        if src not in self.graph:
            self.graph[src] = []
        if dest not in self.graph:
            self.graph[dest] = []

        self.graph[src].append([dest, weight])

        # for undirected graph
        # self.graph[dest].append([src, weight])

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

    def bellmanFordAlgorithm(self, src):

        # s1 distances - distOfNodeFromSrc
        distances = [float('inf')] * len(self.graph)
        distances[src] = 0
        parent = [None] * self.V

        # s2
        for _ in range(len(self.graph) - 1):
            for u in self.graph:
                adjacencyList = self.graph[u]
                for v, w in adjacencyList:
                    if distances[u] != float('inf') and distances[v] > distances[u] + w:
                        distances[v] = distances[u] + w
                        parent[v] = u

        # s3
        for u in self.graph:
            adjacencyList = self.graph[u]
            for v, w in adjacencyList:
                if distances[u] != float('inf') and distances[v] > distances[u] + w:
                    print('contains negative weight cycle')
                    return

        self.printResult(src, distances)

        print('\nPaths from', src, '\nTo \t Path')
        for vertex in self.graph:
            print(vertex, '\t', [src] + self.printPath(vertex, parent))

    def printResult(self, src, distances):

        print('vertex \t distance from', src)
        for vertex in range(len(distances)):
            print(vertex, ' \t ', distances[vertex])

    def printPath(self, idx, parent):

        path = []
        while idx:
            path.append(idx)
            idx = parent[idx]
        return path[::-1]

# code


if __name__ == "__main__":

    g = G(5)
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

    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)

    g.printG()

    print()
    g.bellmanFordAlgorithm(0)

    # g.printG()
