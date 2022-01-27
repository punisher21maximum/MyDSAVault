

def getTransitiveClosure(graph):  # Time O(n^3)
    '''
    Here we take each node (k) one by one,
    as intermediate node in the path.
    If taking node k as intermediate
    there is a path we update the matrix.
    '''
    V = len(graph)
    transitiveClosure = [row[:] for row in graph]

    for i in range(V):
        for u in range(V):
            for v in range(V):
                transitiveClosure[u][v] = transitiveClosure[u][v] or (
                    transitiveClosure[u][i] and transitiveClosure[i][v])

    for row in transitiveClosure:
        print(row)


graph = [[1, 1, 0, 1],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [0, 0, 0, 1]]

getTransitiveClosure(graph)
