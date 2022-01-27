def numOfWaysToMakeChange(denoms, targetSum):
    '''
    Question: We are given denoms array, which has diff denominations,
    like 1, 2, 5, 10,..etc. and a targetSum.
    We can assume we have umlimited num of coins of each denomination.

    We have to find the number of ways we can make targetSum,
    using diff combinations of coins at hand.

    Approach:
    Note for particular targetSum, ways to make change
    with a specific denom is ways[target] = ways[target - denom]

    So using DP approach, we will find the solution 
    for target value 0 to targetSum
    '''
    ways = [0] * (targetSum + 1)
    ways[0] = 1

    for deno in denoms:
        for amt in range(1, targetSum + 1):
            if deno <= amt:
                ways[amt] += ways[amt - deno]

    return ways[-1]
