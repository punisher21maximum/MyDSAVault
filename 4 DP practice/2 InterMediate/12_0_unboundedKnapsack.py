def func(W, weights, values):
    """
    Unbounded means: each item can be used many items.

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
                DP[w][i] = max(values[i - 1] + DP[w - weights[i - 1]][i], DP[w][i - 1])
            else:
                DP[w][i] = DP[w][i - 1]

    for d in DP:
        print(d)


val = [10, 40, 50, 70]
wt = [1, 3, 4, 5]
W = 8
func(W, wt, val)
