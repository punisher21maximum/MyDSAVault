def checkLoop(array):
    '''
    array as graph: index rep node
    how to move to other nodes: 
        nextNode index = (i + arr[i]) % n
        if arr[i] is -ve, move left
    '''

    visited = [False] * len(array)

    for node in range(len(array)):

        adjNode = node
        print('node', node)
        if not visited[adjNode]:
            print('  not vis', adjNode)

            while not visited[adjNode]:
                visited[adjNode] = True
                adjNode = (adjNode + array[adjNode]) % len(array)
                print('    adjNode', adjNode)

            print('      compare', node, adjNode)
            if adjNode == node:
                print('------  cycle', node, end=' ')

                adjNode = (adjNode + array[adjNode]) % len(array)
                while adjNode != node:
                    print(adjNode, end=' ')
                    adjNode = (adjNode + array[adjNode]) % len(array)

                print()


checkLoop([2, -1, 1, 2, 2])
