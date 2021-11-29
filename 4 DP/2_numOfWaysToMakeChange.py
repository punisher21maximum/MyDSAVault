

def numOfWaysToMakeChange(denoms, targetSum):

    ways = [0] * (targetSum + 1)
    ways[0] = 1

    for deno in denoms:
        for amt in range(1, targetSum + 1):
            if deno <= amt:
                ways[amt] += ways[amt - deno]

    return ways[-1]
