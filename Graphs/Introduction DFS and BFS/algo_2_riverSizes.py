def riverSizes(matrix):
    # Write your code here.
    sizes = []
    visited = [[0 for col in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not visited[i][j] and matrix[i][j] == 1:
                traverseNodes(i, j, matrix, visited, sizes)

    for v in visited:
        print(v)
    return sizes


def traverseNodes(i, j, matrix, visited, sizes):

    queue = [[i, j]]
    sizes.append(0)
    while queue:
        i, j = queue.pop(0)

        if visited[i][j]:
            continue

        visited[i][j] = 1
        sizes[-1] += 1

        nodeNeighbours = getValidImmediateNeighbour(i, j, visited, matrix)
        queue.extend(nodeNeighbours)


def getValidImmediateNeighbour(i, j, visited, matrix):

    validNeighbours = []

    # top
    if i-1 >= 0 and not visited[i-1][j] and matrix[i-1][j] == 1:
        validNeighbours.append([i-1, j])
    # left
    if j-1 >= 0 and not visited[i][j-1] and matrix[i][j-1] == 1:
        validNeighbours.append([i, j-1])
    # right
    if j+1 <= len(matrix[i]) - 1 and not visited[i][j+1] and matrix[i][j+1]:
        validNeighbours.append([i, j+1])
    # bottom
    if i+1 <= len(matrix) - 1 and not visited[i+1][j] and matrix[i+1][j]:
        validNeighbours.append([i+1, j])

    return validNeighbours
