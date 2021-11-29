INF = float('inf')


def detectNegativeCycle(graph, V):
    '''
    Approach 1:       
    Keep Two flags: 1. isNegative 2. isCycle 
    if both are true --> negative cycle found 
    flag 1: isNegative: set true if negative edge, set false when done 
    flag 2: isCycle: set true if cycle found 

    Approach 2: Floyd Warshall 
    Distance for a node from itself should be zero,
    if it is not zero, negative cycle.
    '''
    dist = [row[:] for row in graph]  # copy of graph

    for intMedNode in range(V):  # int = intermediateNode
        for u in range(V):
            for v in range(V):
                dist[u][v] = min(dist[u][v],
                                 dist[u][intMedNode] + dist[intMedNode][v])

    for node in range(V):
        if dist[node][node] < 0:
            return True
    return False


graph = [[0, 1, INF, INF],
         [INF, 0, -1, INF],
         [INF, INF, 0, -1],
         [-1, INF, INF, 0]]

print(detectNegativeCycle(graph, 4))
