def minNumberOfJumps(array):

    jumps = [float('inf') for _ in array]
    jumps[0] = 0

    for i in range(len(array)):
        for j in range(0, i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[j] + 1, jumps[i])

    print(jumps[-1])
    return jumps[-1]


minNumberOfJumps([1, 1])
