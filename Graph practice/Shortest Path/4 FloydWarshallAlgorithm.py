INF = float('inf')


def floydWarshallAlgorithm(graph):
    '''
    Shortest Path b/w each pair of nodes Algorithm:
    Here we take each node (k) one by one,
    as intermediate node in the path.
    If taking node k as intermediate
    there is a path and dist is smaller
    we update the dist.
    '''
    V = len(graph)

    for i in range(V):
        for u in range(V):
            for v in range(V):
                graph[u][v] = min(graph[u][i] + graph[i][v], graph[u][v])

    for row in graph:
        print(row)


graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]

floydWarshallAlgorithm(graph)
