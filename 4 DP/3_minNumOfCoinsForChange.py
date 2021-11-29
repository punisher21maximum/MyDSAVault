

def minNumberOfCoinsForChange(denoms, targetSum):

    numOfCoins = [float('inf')] * (targetSum + 1)
    numOfCoins[0] = [0]

    for deno in denoms:
        for amt in range(1, targetSum + 1):
            if deno <= amt:
                numOfCoins[amt] = min(
                    numOfCoins[amt], numOfCoins[amt - deno] + 1)

    return numOfCoins[-1] if numOfCoins[-1] != float('inf') else -1
