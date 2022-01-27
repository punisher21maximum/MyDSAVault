def func(weights, K, N):

    if K == 0:
        return True
    elif N == 0:
        return False
    elif weights[N - 1] <= K:
        return func(weights, K - weights[N - 1], N - 1) or func(weights, K, N - 1)
    else:
        return func(weights, K, N - 1)


weights = [3, 4, 5, 2]
K = 6
N = len(weights)
print(func(weights, K, N))
