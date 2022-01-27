

class G:

    def __init__(self, numOfVertices):
        self.V = numOfVertices
        self.graph = {}

    def addEdge(self, src, dest, weight):

        if src not in self.graph:
            self.graph[src] = []
        if dest not in self.graph:
            self.graph[dest] = []

        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)

        # for undirected graph
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)

    def printG(self):

        for node in self.graph:
            for adjNode in self.graph[node]:
                print(node, ':', adjNode)

# Code

    def getNearestNonVisitedVertex(self, distances, visited):

        minDistance = float('inf')
        minDistanceVertex = None

        for vertex in range(self.V):
            if not visited[vertex] and distances[vertex] < minDistance:
                minDistance = distances[vertex]
                minDistanceVertex = vertex

        return minDistanceVertex

    def printMST(self, distances):

        print('Dikstras MST below \nVertex\tDistance')
        for vertex in range(self.V):
            print(vertex, '\t', distances[vertex])

    def printPathToNode(self, src, path):

        for vertex in range(self.V):
            v = vertex

            pathToNode = [v]

            while path[v] != src:
                pathToNode.append(path[v])
                v = path[v]

            pathToNode.append(src)

            print(vertex, pathToNode[::-1])

    def dijkstra(self, src):

        distances = [float('inf')] * self.V
        visited = [False] * self.V

        # path
        path = [None] * self.V
        path[src] = src

        distances[src] = 0

        for _ in range(self.V):

            # find next node to be added to MST: nearest non-visited node
            u = self.getNearestNonVisitedVertex(distances, visited)

            # mark visited
            visited[u] = True

            # update distances
            for v, w in self.graph[u]:
                if not visited[v] and distances[v] > distances[u] + w:
                    distances[v] = distances[u] + w
                    # path
                    path[v] = u

        self.printMST(distances)
        self.printPathToNode(src, path)


if __name__ == "__main__":

    graph = G(9)
    graph.addEdge(0, 1, 4)
    graph.addEdge(0, 7, 8)
    graph.addEdge(1, 2, 8)
    graph.addEdge(1, 7, 11)
    graph.addEdge(2, 3, 7)
    graph.addEdge(2, 8, 2)
    graph.addEdge(2, 5, 4)
    graph.addEdge(3, 4, 9)
    graph.addEdge(3, 5, 14)
    graph.addEdge(4, 5, 10)
    graph.addEdge(5, 6, 2)
    graph.addEdge(6, 7, 1)
    graph.addEdge(6, 8, 6)
    graph.addEdge(7, 8, 7)

    # graph.printG()

    graph.dijkstra(0)
