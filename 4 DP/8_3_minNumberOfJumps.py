def minNumberOfJumps(array):

    if len(array) == 1:
        return 0

    jumps = 0
    steps = array[0]
    maxReach = array[0]

    for i in range(1, len(array)):
        maxReach = max(maxReach, i + array[i])

        steps -= 1

        if steps == 0:
            steps = maxReach - i
            jumps += 1
        elif i == len(array) - 1:
            jumps += 1

    return jumps


print(minNumberOfJumps([3, 4, 2, 1, 2, 3, 4, 1, 1, 1, 3]))
