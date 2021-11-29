def countMagicalNodes(array):
    '''
    Magical Index -
    index i and j are connected if j = (i + arr[i]) % n + 1
    traversing this way if same index visited again, then it is magical index

    array as graph:
    each index denotes a node
    value at that index (arr[i]) gives node to which it is connected
    '''

    count = 0
    visited = [0] * (len(array) + 1)
    parent = [-1] * (len(array) + 1)

    for node in range(len(array)):

        adjNode = node

        if parent[adjNode] == -1:  # not visited

            while parent[adjNode] == -1:
                parent[adjNode] = node
                adjNode = (node + array[node]) % len(array) + 1

            if parent[adjNode] == node:

                while not visited[adjNode]:
                    visited[adjNode] = 1

                    count += 1

                    adjNode = (node + array[node]) % len(array) + 1

    print(count)


countMagicalNodes([0, 0, 0, 2])
