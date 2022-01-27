def isSafe(node, color, colorMap):

    adjList = graph[node]
    for adjNode in adjList:
        if adjNode in colorMap and colorMap[adjNode] == color:
            return False
    return True


def mapColoringBackTrackHelper(node, colors, colorMap):

    for color in colors:
        if isSafe(node, color, colorMap):
            colorMap[node] = color
            for node in graph:
                if node not in


def mapColoringBackTrack(graph, M):
    '''

    '''
    colors = [i for i in range(1, M+1)]
    colorMap = dict()
    for node in graph:
        mapColoringBackTrackHelper(node, colors, colorMap)


graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
M = 3
mapColoringBackTrack(graph, M)
