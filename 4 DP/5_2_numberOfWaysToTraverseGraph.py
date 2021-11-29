def numberOfWaysToTraverseGraph(width, height):

    ways = [[0 for w in range(width+1)] for h in range(height+1)]

    for i in range(1, height+1):
        for j in range(1, width+1):
            if i == 1 or j == 1:
                ways[i][j] = 1
            else:
                ways[i][j] = ways[i][j-1] + ways[i-1][j]

    return ways[-1][-1]
