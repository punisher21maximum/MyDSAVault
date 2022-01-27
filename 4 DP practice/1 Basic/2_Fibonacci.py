def getNthFibonacciNum(N):
    """
    Given - a number N, print Nth fibonacci number (1 indexing)

    F(N) = F(N-2) + F(N-1)
    """

    if N < 0:
        return -1
    elif N == 0:
        return 0
    elif N == 1:
        return 1

    DP = [0, 1] + [0] * (N - 2)

    for i in range(2, N):
        DP[i] = DP[i - 2] + DP[i - 1]

    print(DP, DP[N - 1])


getNthFibonacciNum(10)
