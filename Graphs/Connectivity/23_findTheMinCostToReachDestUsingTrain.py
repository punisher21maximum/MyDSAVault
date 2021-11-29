def findTheMinCostToReachDestUsingTrain(graph):

    V = len(graph)
    srcStation, destStation = 0, V - 1

    path = [srcStation]
    minCost = graph[srcStation][destStation]

    findTheMinCostToReachDestUsingTrainHelper(
        graph, srcStation, destStation, path, minCost, cost=0)


def findTheMinCostToReachDestUsingTrainHelper(graph, srcStation, destStation,
                                              path, minCost, cost):

    if srcStation == destStation:
        print('Cost', minCost, ': Path', path)

    adjStationsList = list(range(srcStation + 1, destStation + 1))
    print('--', srcStation)
    for adjStation in adjStationsList:

        path.append(adjStation)
        cost += graph[srcStation][adjStation]

        if adjStation == destStation:
            minCost = min(cost, minCost)

        findTheMinCostToReachDestUsingTrainHelper(graph, adjStation, destStation,
                                                  path, minCost, cost)

        path.pop()
        cost -= graph[srcStation][adjStation]


graph = [[0, 15, 80, 90],
         [float("inf"), 0, 40, 50],
         [float("inf"), float("inf"), 0, 70],
         [float("inf"), float("inf"), float("inf"), 0]
         ]

findTheMinCostToReachDestUsingTrain(graph)
