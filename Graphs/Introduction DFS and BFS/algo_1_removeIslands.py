def removeIslands(matrix):
    # Write your code here.
    visited = [[False for col in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not visited[i][j] and matrix[i][j] == 1 and not isBorderTouch(i, j, matrix):
                removeIfIsland(i, j, visited, matrix)

        return matrix


def removeIfIsland(i, j, visited, matrix):

    queue = [[i, j]]
    island = [[i, j]]
    borderTouch = False
    while queue:
        i, j = queue.pop(0)

        visited[i][j] = True
        if isBorderTouch(i, j, matrix):
            borderTouch = True

        unvisitedNeighbours = unvisitedValidNeighbours(i, j, visited, matrix)
        queue.extend(unvisitedNeighbours)
        island.extend(unvisitedNeighbours)

    if not borderTouch:
        for i, j in island:
            matrix[i][j] = 0

    print('rm island', island)


def isBorderTouch(i, j, matrix):

    return i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[i]) - 1


def unvisitedValidNeighbours(i, j, visited, matrix):

    neighbours = []

    if j-1 >= 0 and not visited[i][j-1] and matrix[i][j-1] == 1:
        neighbours.append([i, j-1])
        print('left')

    if i-1 >= 0 and not visited[i-1][j] and matrix[i-1][j] == 1:
        neighbours.append([i-1, j])
        print('up')

    if j+1 <= len(matrix[i]) - 1 and not visited[i][j+1] and matrix[i][j+1] == 1:
        neighbours.append([i, j+1])
        print('right')

    if i+1 <= len(matrix) - 1 and not visited[i+1][j] and matrix[i+1][j] == 1:
        neighbours.append([i+1, j])
        print('down')

    return neighbours
