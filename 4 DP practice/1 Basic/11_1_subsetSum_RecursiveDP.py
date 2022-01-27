def func(weights, K, N, DP):
    print(K, N, weights[N - 1])
    if K == 0:
        DP[K][N] = True
    elif N == 0:
        DP[K][N] = False
    elif weights[N - 1] <= K:
        DP[K][N] = func(weights, K - weights[N - 1], N - 1, DP) or func(
            weights, K, N - 1, DP
        )
    else:
        DP[K][N] = func(weights, K, N - 1, DP)

    return DP[K][N]


weights = [3, 4, 5, 2]
K = 6
N = len(weights)
DP = [[None for c in range(N + 1)] for r in range(K + 1)]
print(func(weights, K, N, DP))
for dp in DP:
    print(dp)
