def func(W, weights, values):
    """
    Problem: Given a sack of items, each item has some weight
    and value. We are given a sack, of maxCapacity (W).
    We have to pick items where total weight of picked items
    is within maxCapacity while maximising the total value.

    Given: weight array, values array, W int
    Each item has weight wights[i] and value values[i].
    MaxCapacity is W.

    DP Approach: We increase the capcaity of sack from 0 to W,
    by 1 unit every time.
    And for each capacity, we traverse all the items, and for
    each item we find if the item can fit in the sack.
    If yes, we find only pick it if it will inc total value
    else we keep the old value.

    Note: When sack size is 0, max total value will be always 0.
    When sack size is not zero but we have zero items, then
    also total value is zero.

    Time O(N*W) | Space O(N*W)
    """
    N = len(weights)  # num of items
    DP = [[None for i in range(N + 1)] for j in range(W + 1)]

    for i in range(N + 1):
        for w in range(W + 1):
            if w == 0:  # sack size 0
                DP[w][i] = 0
            elif i == 0:  # 0 items
                DP[w][i] = 0
            elif weights[i - 1] <= w:
                DP[w][i] = max(
                    values[i - 1] + DP[w - weights[i - 1]][i - 1], DP[w][i - 1]
                )
            else:
                DP[w][i] = DP[w][i - 1]

    for d in DP:
        print(d)


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
func(W, wt, val)
