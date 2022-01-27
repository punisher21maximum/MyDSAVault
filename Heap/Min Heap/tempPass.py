def minPotsToRemove(N, a):
    if N == 0:
        return 0
    if N == 1:
        return 0

    result = 0

    for i in range(1, N):
        if a[i] > a[i-1]:
            extraPots = a[i] - a[i-1]
            a[i] -= extraPots
            result += extraPots

    return result


N = int(input())
a = list(map(int, input().split()))

print(minPotsToRemove(N, a))  # list(map(int, '1 2 3 4 5'.split())
