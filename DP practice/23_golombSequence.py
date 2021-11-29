def golombSequence(N):

    sequence = ['X', 1, 2, 2]  # use 1 indexing

    for nth in range(3, N + 1):
        numOfNth = sequence[nth]

        for _ in range(numOfNth):
            sequence.append(nth)

            if len(sequence) >= N:
                return sequence


print(golombSequence(20))
