def golombSequenceArray(N):

    sequence = [0] * (N + 1)

    sequence[1] = 1

    for i in range(2, N + 1):
        sequence[i] = 1 + sequence[i - sequence[sequence[i - 1]]]

    print(sequence)


# golombSequenceArray(30)


def findGolomb(N):
    if N == 1:
        return 1
    else:
        return 1 + findGolomb(N - findGolomb(findGolomb(N - 1)))


for i in range(1, 20):
    print(findGolomb(i), end=" ")
