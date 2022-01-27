def func(W, weights, values):
    """
    printItems

    Time O(N*W) | Space O(N*W)
    """
    N = len(weights)  # num of items
    DP = [[None for i in range(N + 1)] for j in range(W + 1)]

    for i in range(N + 1):
        for w in range(W + 1):
            if w == 0:  # sack size 0
                DP[w][i] = 0
            elif i == 0:  # 0 items
                DP[w][i] = 0
            elif weights[i - 1] <= w:
                DP[w][i] = max(
                    values[i - 1] + DP[w - weights[i - 1]][i - 1], DP[w][i - 1]
                )
            else:
                DP[w][i] = DP[w][i - 1]

    for d in DP:
        print(d)
    printKnapsackItems(DP, weights, values, W, N)


def printKnapsackItems(DP, weights, values, W, N):
    items = []
    r, c = W, N
    while DP[r][c] != 0:
        if DP[r][c] == DP[r][c - 1]:
            c -= 1
        else:
            items.append([weights[c - 1], values[c - 1]])
            c -= 1
            r -= weights[c - 1]
    print(items[::-1])


val = [6, 10, 12]
wt = [1, 2, 3]
W = 5
func(W, wt, val)
