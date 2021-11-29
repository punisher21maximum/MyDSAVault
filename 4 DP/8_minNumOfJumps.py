def minNumberOfJumps(array):

    if len(array) == 1:
        return 0
    jumps = 0
    flag = 0
    nextJumpIdx = 0
    currentJumpRange = array[0]
    sequence = []

    idx = 0
    while idx < len(array):
        nextMaxJumpRange = currentJumpRange
        print(idx, end=' ')
        for i in range(idx + 1, idx + 1 + currentJumpRange):
            print(i, end=' ')
            if i == len(array) - 1:
                flag = 1
                break

            jumpRange = i + array[i]
            if jumpRange > nextMaxJumpRange:
                nextMaxJumpRange = i + array[i]
                nextJumpIdx = i

        jumps += 1
        sequence.append(array[nextJumpIdx])

        idx = nextJumpIdx
        currentJumpRange = array[nextJumpIdx]

        if flag:
            break

    print(jumps, sequence)
    return jumps


minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3])
