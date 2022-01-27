def func(weights, maxCapacity):
    """
    Problem - Find max sum from 'weights' array, by summing
    the elements while keeping the under maxCapacity

    Approach - Problem is same as 0/1 Knapsack.
    0/1 Knapsack problem:
    Given> maxCapacity(int), weights(array) and values(array).
    Find> max "value" by choosing items with total sum within
    maxCapacity.

    In this question:
    Given> maxCapacity(int) and weights(array).
    Find> max "weight" by choosing items with total sum within
    maxCapacity.

    Difference:
    So unlike knapsack have to maximise weight
    instead of values. Thus, weight array will work as values
    array here.
    """
    knapsack = [[0 for i in range(len(weights) + 1)] for j in range(maxCapacity + 1)]

    for w in range(maxCapacity + 1):
        for i in range(len(weights) + 1):
            if i == 0 or w == 0:
                knapsack[w][i] = 0
            elif weights[i - 1] <= w:
                knapsack[w][i] = max(
                    weights[i - 1] + knapsack[w - weights[i - 1]][i - 1],
                    knapsack[w][i - 1],
                )
            else:
                knapsack[w][i] = knapsack[w][i - 1]

    for r in knapsack:
        print(r)


func([4, 8, 5, 9], 20)
