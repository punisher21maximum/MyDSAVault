from typing import DefaultDict


def golombSequence(N):

    sequence = ['X', 1, 2, 2]  # use 1 indexing
    f = {1: 1, 2: 1}
    for num in range(3, N + 1):
        freq = sequence[num]
        # print(num, freq)
        if freq not in f:
            f[freq] = 1
        else:
            f[freq] += 1
        for _ in range(freq):
            sequence.append(num)

            if len(sequence) + 1 >= N:
                return sequence

    print(f)


# print(['X'] + list(range(1, 21)))
fOfF = golombSequence(10000)
# print(fOfF)
fOfFofF = DefaultDict()
for key in fOfF:
    if fOfF[key] not in fOfFofF:
        fOfFofF[fOfF[key]] = 1
    else:
        fOfFofF[fOfF[key]] += 1
print('--.', fOfFofF)
