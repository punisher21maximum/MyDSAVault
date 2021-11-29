

def totalNumOfSpanningTrees(graph):
    '''
    Algo:
    s1: fill the diagonal with degree of node
    s2: set all non-diagonal elements as -1
    s3: find co-factor of any diagonal element
    '''
    for node in range(len(graph)):
        for adjNode in range(len(graph)):
            if node != adjNode and graph[node][adjNode] == 1:
                graph[node][node] += 1  # s1
                graph[node][adjNode] = -1  # s2

    # find co-factor of any diagonal element
