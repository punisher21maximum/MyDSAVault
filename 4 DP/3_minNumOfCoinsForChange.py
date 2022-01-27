def minNumberOfCoinsForChange(denoms, targetSum):
    '''
    Question: Given denoms and tagretSum
    find min num of coins to make targetSum.

    Approach:
    Note for a target ways to make change
    with particular deno is, ways[target] = 1 + ways[target - deno]


    min(ways[target], 1 + ways[target - deno])
    '''

    numOfCoins = [float('inf')] * (targetSum + 1)
    numOfCoins[0] = [0]

    for deno in denoms:
        for amt in range(1, targetSum + 1):
            if deno <= amt:
                numOfCoins[amt] = min(
                    numOfCoins[amt], numOfCoins[amt - deno] + 1)

    return numOfCoins[-1] if numOfCoins[-1] != float('inf') else -1
