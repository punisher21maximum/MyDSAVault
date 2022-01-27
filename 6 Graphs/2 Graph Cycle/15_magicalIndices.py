def countMagicalIndicesHelper(array, node, currNode, visited):

    if visited[currNode]:
        if node == currNode:
            return 1
        else:
            return 0
    else:
        visited[currNode] = True

    nextNode = (currNode + array[currNode]) % len(array) + 1

    return countMagicalIndicesHelper(array, node, nextNode, visited)


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

    for node in range(len(array)):

        visited = [False] * len(array)
        visited[node] = True

        nextNode = (node + array[node]) % len(array) + 1

        count += countMagicalIndicesHelper(array,
                                           node, nextNode, visited)

    print(count)


countMagicalNodes([0, 0, 0, 2])
