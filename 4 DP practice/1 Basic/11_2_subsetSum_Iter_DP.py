def func(weights, K):
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
    Find - need to find the subset with given sum.

    Difference from knapsack:
    We have to to stop once the sum of elements is ET K,
    unlike knapsack where we aim to maximise the total weight
    (or total value).

    Time O(N*K) | Space O(N*K), N is len of arr.

        0   3   4   5   2
    0   T   T   T   T   T
    1   F   F   F   F   F
    2   F   F   F   F   T
    3   F   T   T   T   T
    4   F   F   T   T   T
    5   F   F   F   T   T
    6   F   F   F   F   T

    Now we know to find the value of current cell,
    we need only the previous columns, not other col
    than that.

    So we will have just two cols, and fill all rows
    for the columns. Once we have filled all values
    in the column, we ensure to make it as prev col
    and set refill current col.
    """
    N = len(weights)
    DP = [[None for c in range(N + 1)] for r in range(K + 1)]

    for n in range(N + 1):
        for k in range(K + 1):
            if k == 0:  # required sum is 0 and setSize does not matter
                DP[k][n] = True
            elif n == 0:  # required sum != 0 and setSize is 0
                DP[k][n] = False
            elif weights[n - 1] <= k:
                DP[k][n] = DP[k][n - 1] or DP[k - weights[n - 1]][n - 1]
            else:
                DP[k][n] = DP[k][n - 1]

    for dp in DP:
        print(dp)


func([3, 4, 5, 2], 6)
