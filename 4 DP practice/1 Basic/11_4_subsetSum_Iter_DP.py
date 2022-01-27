def func(arr, K):
    """
    Problem - Given a array with integers and an integer K.
    Find if there exist a subset with sum equal to K.
    Subset does not need to be continous.

    Tags - [choosing subset from array for given conditions,
    similar to 0/1 knapsack]

    Approach - Similar to 0/1 knapsack.
    Knapsack:
    Given - weights (int arr), maxCapacity (int)
    Find - max sum of weights where total weight LE maxCapacity.

    This Q:
    Given - array/weights (int arr), K (int)
    Find - need to find the subset wuth given sum.

    Difference from knapsack:
    We have to to stop once the sum of elements is ET K,
    unlike knapsack where we aim to maximise the total weight
    (or total value).
    """

    DP = [[True for i in range(2)] for j in range(K + 1)]

    for k in range(K + 1):
        for j in range(len(arr) + 1):
            if k == 0:
                """
                When required sum (k) is 0
                """
                DP[k][j] = True
            elif k != 0 and j == 0:
                """
                When K != 0 and weights is empty
                """
                DP[k][j] = False
            elif arr[j - 1] <= k:
                DP[k][j] = DP[k][j - 1] or (DP[k - arr[j - 1]][j - 1])
            else:
                DP[k][j] = DP[k][j - 1]

    print(DP[-1][-1])
    print(DP)


func([3, 34, 4, 12, 5, 2], 9)
