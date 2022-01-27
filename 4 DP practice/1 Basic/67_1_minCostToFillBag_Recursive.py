def func2(weights, values, W, N):
    """ """
    if W == 0:
        return 0
    elif N == 0:
        return float("inf")
    elif weights[N - 1] <= W:
        return min(
            func2(weights, values, W, N - 1),
            values[N - 1] + func2(weights, values, W - weights[N - 1], N),
        )
    else:
        return func2(weights, values, W, N - 1)


def func(costs, W):
    values = []
    weights = []
    for i in range(len(costs)):
        if costs[i] != -1:
            values.append(costs[i])
            weights.append(i + 1)
    N = len(values)
    print(values, weights, W, N)
    result = func2(weights, values, W, N)
    return result if result != float("inf") else -1


print(func([10, -1, -1, -1, -1], 5))
