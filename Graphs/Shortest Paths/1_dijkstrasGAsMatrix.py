

class G:

    def __init__(self, numOfVertices):
        self.V = numOfVertices
        self.graph = [[0 for col in range(numOfVertices)]
                      for row in range(numOfVertices)]

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

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

        for vertex in range(self.V):
            print('V: ', vertex, ' dist ', distances[vertex])

    def dijkstra(self, src):

        distances = [float('inf')] * self.V
        visited = [False] * self.V

        distances[src] = 0

        for _ in range(self.V):

            # get non-visited node at minimum distance
            u = self.getNearestNonVisitedVertex(distances, visited)
            visited[u] = True

            # update distances
            for v in range(self.V):
                if self.graph[u][v] > 0 and not visited[v] and \
                        distances[v] > distances[u] + self.graph[u][v]:
                    distances[v] = distances[u] + self.graph[u][v]

        self.printMST(distances)


if __name__ == "__main__":

    g = G(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.dijkstra(0)
