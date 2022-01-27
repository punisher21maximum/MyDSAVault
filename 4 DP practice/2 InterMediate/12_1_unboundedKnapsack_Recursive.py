def func(W, weights, values, N):
    """
    Same as - "12_0_unboundedKnapsack.py"

    Recursive

    Time O(N*W) | Space O(N*W)
    """
    if W == 0:
        return 0
    elif N == 0:
        return 0
    elif weights[N - 1] <= W:
        return max(
            values[N - 1] + func(W - weights[N - 1], weights, values, N),
            func(W, weights, values, N - 1),
        )
    else:
        return func(W, weights, values, N - 1)


val = [10, 40, 50, 70]
wt = [1, 3, 4, 5]
W = 8
print(func(W, wt, val, len(wt)))
