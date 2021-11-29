def postorderFromInorderAndPreorder(inorder, preorder, postorder):

    if len(preorder) == 0:
        return

    root = preorder[0]
    for i in range(len(inorder)):
        if inorder[i] == root:
            rootIdx = i
            break

    lennOfLeftSubtree = len(inorder[:rootIdx])
    lennOfRightSubtree = len(inorder[rootIdx + 1:])

    postorderFromInorderAndPreorder(
        inorder[: rootIdx], preorder[1: 1 + lennOfLeftSubtree], postorder)
    postorderFromInorderAndPreorder(
        inorder[rootIdx + 1:], preorder[1 + lennOfLeftSubtree:], postorder)
    postorder.append(preorder[0])


inorder = [4, 2, 5, 1, 6, 3, 7]
preorder = [1, 2, 4, 5, 3, 6, 7]
postorder = []
postorderFromInorderAndPreorder(inorder, preorder, postorder)
print(postorder)
correctPostorder = [4, 5, 2, 6, 7, 3, 1]
if postorder == correctPostorder:
    print('Correct')
