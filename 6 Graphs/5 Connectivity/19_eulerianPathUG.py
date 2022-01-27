def findIfEulerianPathPossibleAndStartNode(graph, V):

    numOfOddDegreeNodes = 0
    startNode = None

    for node in range(V-1, -1, -1):
        degreeOfCurrNode = sum(graph[node])

        if (degreeOfCurrNode % 2) == 1:  # odd
            numOfOddDegreeNodes += 1
            startNode = node

        if numOfOddDegreeNodes > 2:
            print('Eulerian Path Not Possible')
            return -1

    print('startNode', startNode)
    return startNode


def findEulerianPathUsingStartNode(graph, V):

    startNode = findIfEulerianPathPossibleAndStartNode(graph, V)
    if startNode == -1:
        return []

    stack = []
    path = []
    currNode = startNode

    while stack or sum(graph[currNode]) != 0:

        numOfAdjNodes = sum(graph[currNode])

        if numOfAdjNodes == 0:
            path.append(currNode)
            currNode = stack.pop()
        else:
            for adjNode in range(V):
                edge = graph[currNode][adjNode]
                if edge == 1:
                    stack.append(currNode)

                    graph[currNode][adjNode] = 0
                    graph[adjNode][currNode] = 0

                    currNode = adjNode

                    break

    return path + [currNode]


def eulerianPathUG(graph, V):
    '''
    Eulerian Path
    1. connected G
    2. 0 or 2 odd-degree nodes
       other even-degree nodes.

    Algorithm:
    1. Find if Eulerian Path possible, if yes find start node:
    if no odd-degree nodes, we can start path from any node
    if 0 or 2 odd-degree nodes, we have to start from these nodes
    if >2 odd-degree nodes, Eulerian Path does not exist.

    2. If currNode has >=1 adjNode, first visit the adjNode,
    then the currNode: 
    create empty stack and empty path
    if currNode has adjNode, push currNode to stack, delete the edge (node, adjNode)
    visit adjNode
    if currNode has no adjNode, pop stack, and visit popped node
    '''

    path = findEulerianPathUsingStartNode(graph, V)

    print(path)


# Test case 1
graph1 = [[0, 1, 0, 0, 1],
          [1, 0, 1, 1, 0],
          [0, 1, 0, 1, 0],
          [0, 1, 1, 0, 0],
          [1, 0, 0, 0, 0]]
n = len(graph1)
eulerianPathUG(graph1, n)

# Test case 2
graph2 = [[0, 1, 0, 1, 1],
          [1, 0, 1, 0, 1],
          [0, 1, 0, 1, 1],
          [1, 1, 1, 0, 0],
          [1, 0, 1, 0, 0]]
n = len(graph2)
eulerianPathUG(graph2, n)

# Test case 3
graph3 = [[0, 1, 0, 0, 1],
          [1, 0, 1, 1, 1],
          [0, 1, 0, 1, 0],
          [0, 1, 1, 0, 1],
          [1, 1, 0, 1, 0]]
n = len(graph3)
eulerianPathUG(graph3, n)

# %%
