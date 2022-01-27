'''
method 2: Create Tree
1. build Tree
2. find height
'''


def buildTreeAsAdjacencyLists(parent):

    root = None
    treeAsDictOfAdjacencyLists = dict()

    for child in range(len(parent)):
        if parent[child] == -1:
            root = child
            treeAsDictOfAdjacencyLists[child] = []
        else:
            if parent[child] not in treeAsDictOfAdjacencyLists:
                treeAsDictOfAdjacencyLists[parent[child]] = [child]
            else:
                treeAsDictOfAdjacencyLists[parent[child]].append(child)

    print(treeAsDictOfAdjacencyLists)
    getHeightForTreeAsAdjacencyLists(root, treeAsDictOfAdjacencyLists, parent)


def getHeightForTreeAsAdjacencyLists(root, treeAsDictOfAdjacencyLists, parent):

    nodesHeight = dict()
    nodesHeight[root] = 0

    treeHeight = nodesHeight[root]

    queue = treeAsDictOfAdjacencyLists[root]

    while queue:
        node = queue.pop(0)

        nodesHeight[node] = nodesHeight[parent[node]] + 1
        treeHeight = max(nodesHeight[node], treeHeight)

        if node in treeAsDictOfAdjacencyLists:
            queue.extend(treeAsDictOfAdjacencyLists[node])

    print(nodesHeight)
    print('treeHeight', treeHeight)


parent = [-1, 0, 0, 0, 3, 1, 1, 2]
buildTreeAsAdjacencyLists(parent)
