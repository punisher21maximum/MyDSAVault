# O(V^3)


def printReach(reach):
    for row in reach:
        print(row)
    print()


def trasitiveClosure(graph, V):

    reach = [[0 for col in row] for row in graph]
    print(reach)

    for node in range(V):
        for node2 in range(V):
            for node3 in range(V):
                if (graph[node][node2] == 1 and graph[node2][node3] == 1):
                    reach[node][node3] = 1

        printReach(reach)


# graph = [[1, 1, 0, 1],
#          [0, 1, 1, 0],
#          [0, 0, 1, 1],
#          [0, 0, 0, 1]]

graph = [[1, 1, 1, 0],
         [0, 1, 1, 0],
         [1, 0, 1, 1],
         [0, 0, 0, 1]]


trasitiveClosure(graph, V=4)
