def findDepth(tree, idx=0, currHeight=0, height=0):

    height = max(currHeight, height)
    print(idx, tree[idx], currHeight, height)
    if tree[idx] == 'l':
        return idx + 1, height

    # print(idx, tree[idx], height)
    height = max(currHeight, height)
    if tree[idx] == 'n':
        idx, height = findDepth(tree, idx + 1, currHeight + 1, height)
    else:
        idx += 1
    print('-', idx, tree[idx], currHeight, height)
    # height = max(currHeight, height)
    currHeight = height
    if tree[idx] == 'n':
        idx, height = findDepth(tree, idx + 1, currHeight + 1, height)
    else:
        idx += 1

    # print(idx, tree[idx], height)
    return idx, height


print(findDepth("nnnnllnllnnllnnllnnnllnllnnllnll"))
s = 'nnnnllnllnnllnnllnnnllnllnnllnll'
