def nearestNonVisitedNode(V, visited, distances):

    minDist = float('inf')
    minDistNode = None

    for node in range(V):
        if not visited[node] and distances[node] < minDist:
            minDist = distances[node]
            minDistNode = node

    return minDistNode


def minimumCostToConnectAllCities(V, graph, src=0):

    distances = [float('-inf')] * V
    visited = [False] * V
    parent = [-1] * V
    cost = 0

    distances[src] = 0

    for _ in range(V-1):

        u = nearestNonVisitedNode(V, visited, distances)

        visited[u] = True

        for v in range(V):
            if graph[u][v] and not visited[v] and distances[v] > graph[u][v]:
                distances[v] = graph[u][v]
                parent[v] = u

    for i in range(1, V):
        cost += graph[parent[i]][i]

    print(cost)


if __name__ == '__main__':

    # Input 1
    n1 = 5
    city1 = [[0, 1, 2, 3, 4],
             [1, 0, 5, 0, 7],
             [2, 5, 0, 6, 0],
             [3, 0, 6, 0, 0],
             [4, 7, 0, 0, 0]]
    minimumCostToConnectAllCities(n1, city1)

    # Input 2
    n2 = 6
    city2 = [[0, 1, 1, 100, 0, 0],
             [1, 0, 1, 0, 0, 0],
             [1, 1, 0, 0, 0, 0],
             [100, 0, 0, 0, 2, 2],
             [0, 0, 0, 2, 0, 2],
             [0, 0, 0, 2, 2, 0]]
    minimumCostToConnectAllCities(n2, city2)
