def func(W, weights, values, N):
    """
    Same as - "10_01knapsack.py"

    Recursive

    Time O(N*W) | Space O(N*W)
    """
    if W == 0:
        return 0
    elif N == 0:
        return 0
    elif weights[N - 1] <= W:
        return max(
            values[N - 1] + func(W - weights[N - 1], weights, values, N - 1),
            func(W, weights, values, N - 1),
        )
    else:
        return func(W, weights, values, N - 1)


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print(func(W, wt, val, len(wt)))
