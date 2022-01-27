def func(W, weights, values):
    """
    Same as - "10_01knapsack.py"

    Time O(N*W) | Space O(W)
    """
    N = len(weights)  # num of items
    DP = [None for _ in range(W + 1)]

    for i in range(N + 1):
        for w in range(W, -1, -1):
            if w == 0:  # sack size 0
                DP[w] = 0
            elif i == 0:  # 0 items
                DP[w] = 0
            elif weights[i - 1] <= w:
                DP[w] = max(values[i - 1] + DP[w - weights[i - 1]], DP[w])

    for d in DP:
        print(d)


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
func(W, wt, val)
