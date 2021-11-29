def detectNegativeWeightCycleFloydWarshall(graphMatrix):

    V = len(graphMatrix)
    distances = [[graphMatrix[i][j] for i in range(V)] for j in range(V)]

    for srcNode in range(V):
        for destNode in range(V):
            for intermediateNode in range(V):
                if (distances[srcNode][destNode] > distances[srcNode][intermediateNode] +
                        distances[intermediateNode][destNode]):
                    distances[srcNode][destNode] = distances[srcNode][intermediateNode] + \
                        distances[intermediateNode][destNode]

    for node in range(V):
        if distances[node][node] < 0:
            print('Negative Weight Cycle')
            return

    print('No cycle')


graph = [[0, 1, float('inf'), float('inf')],
         [float('inf'), 0, -1, float('inf')],
         [float('inf'), float('inf'), 0, -1],
         [-1, float('inf'), float('inf'), 0]]

detectNegativeWeightCycleFloydWarshall(graph)
