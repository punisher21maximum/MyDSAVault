
class G:

    def __init__(self, V):
        self.graph = []
        self.V = V

    def addEdge(self, u, v, w):

        self.graph.append([u, v, w])

    def printG(self):

        for u, v, w in self.graph:
            print(u, v, w)

    def bellmanFordAlgorithm(self, src):

        distances = [float('inf')] * self.V
        distances[src] = 0
        parent = [None] * self.V

        for _ in range(self.V):
            for u, v, w in self.graph:
                if distances[u] != float('inf') and distances[v] > distances[u] + w:
                    distances[v] = distances[u] + w
                    parent[v] = u

        for u, v, w in self.graph:
            if distances[u] != float('inf') and distances[v] > distances[u] + w:
                print('Negative Weight')
                return

        self.printResult(src, distances)

        print('\nPaths from', src, '\nTo \t Path')
        for vertex in range(self.V):
            print(vertex, '\t', [src] + self.printPath(vertex, parent))

    def printResult(self, src, distances):

        print('src: ', src)
        print('vertex \t distance from src')
        for vertex in range(len(distances)):
            print(vertex, '\t', distances[vertex])

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
