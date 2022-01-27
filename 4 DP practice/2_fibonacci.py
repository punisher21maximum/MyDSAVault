def nthFibonacciNum(N):
    # bottom up

    fibs = [0, 1]

    for n in range(2, N+1):
        fibs[n] = fibs[n-1] + fibs[n-2]

    return fibs[N]


def fibonacci(N):
    # top down
    if N < 1:
        return -1
    if N == 1:
        return 1
    elif N == 2:
        return 2
    return fibonacci(N-1) + fibonacci(N-2)


# for i in range(1, 9):
print(fibonacci(9))
