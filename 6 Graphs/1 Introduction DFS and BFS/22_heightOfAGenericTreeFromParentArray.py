

# Code

def getHeightOfGenericTreeFromParentArray(parent):
    '''
    method 1: Not creating Tree
    find the level from root to bottom
    '''
    nodesLeft = len(parent)
    parentLevel = dict()
    treeHeight = -1

    for child in range(len(parent)):
        if parent[child] == -1:
            currentParent = child
            parentLevel[currentParent] = 0

            nodesLeft -= 1
            treeHeight += 1

            break

    print(parentLevel)

    while nodesLeft:

        for child in range(len(parent)):
            if parent[child] in parentLevel:
                parentLevel[child] = parentLevel[parent[child]] + 1
                print(child, parent[child], parentLevel[parent[child]]+1)

                nodesLeft -= 1
                treeHeight = max(parentLevel[child], treeHeight)

    print(parentLevel)
    print(treeHeight)


if __name__ == "__main__":

    parent = [-1, 0, 0, 0, 3, 1, 1, 2]
    getHeightOfGenericTreeFromParentArray(parent)
