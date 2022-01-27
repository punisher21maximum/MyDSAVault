def waterJugProblemUsingBFS(jug1max, jug2max, target):

    visited = dict()
    visited[(jug1max, jug2max)] = True
    print(visited)
    queue = [[0, 0]]

    while queue:
        jug1, jug2 = queue.pop()

        if jug1 == target or jug2 == target:
            print('found')

        visited[(jug1, jug2)] = True

        nextValidStates = getValidStates(visited, jug1, jug2, jug1max, jug2max)
        print(jug1, jug2, nextValidStates)
        queue.extend(nextValidStates)


def getValidStates(visited, jug1, jug2, jug1max, jug2max):

    nextValidStates = []

    # Empty
    #  j1
    if (0, jug2) not in visited:
        nextValidStates.append([0, jug2])
    #  j2
    if (jug1, 0) not in visited:
        nextValidStates.append([jug1, 0])

    # Full
    #  j1
    if (jug1max, jug2) not in visited:
        nextValidStates.append([jug1max, jug2])
    #  j2
    if (jug1, jug2max) not in visited:
        nextValidStates.append([jug1, jug2max])

    # Move
    #  j1 to j2
    d12 = min(jug1, jug2max - jug2)
    if (jug1 - d12, jug2 + d12) not in visited and d12 > 0:
        nextValidStates.append([jug1 - d12, jug2 + d12])
    #  j2 to j1
    d21 = min(jug1max - jug1, jug2)
    if (jug1 + d21, jug2 - d21) not in visited and d21 > 0:
        nextValidStates.append([jug1 + d21, jug2 - d21])

    return nextValidStates


waterJugProblemUsingBFS(jug1max=4, jug2max=3, target=2)
