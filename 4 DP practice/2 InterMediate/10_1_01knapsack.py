def func(W, weights, values):
    """
    Same as - "10_01knapsack.py"

    Time O(N*W) | Space O(2*W)
    """
    N = len(weights)  # num of items
    DP = [[None for i in range(2)] for j in range(W + 1)]

    for i in range(N + 1):
        for w in range(W + 1):
            if w == 0:  # sack size 0
                DP[w][i % 2] = 0
            elif i == 0:  # 0 items
                DP[w][i % 2] = 0
            elif weights[i - 1] <= w:
                DP[w][i % 2] = max(
                    values[i - 1] + DP[w - weights[i - 1]][(i - 1) % 2],
                    DP[w][(i - 1) % 2],
                )
            else:
                DP[w][i % 2] = DP[w][(i - 1) % 2]

    for d in DP:
        print(d)


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
func(W, wt, val)
