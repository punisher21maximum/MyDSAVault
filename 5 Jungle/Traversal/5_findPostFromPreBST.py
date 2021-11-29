def postorderFromPreorderBST(preorder, postorder):

    if len(preorder) == 0:
        return

    firstIdxOfRightSubTree = 1
    for idx in range(1, len(preorder)):
        if preorder[idx] > preorder[0]:
            firstIdxOfRightSubTree = idx
            break

    postorderFromPreorderBST(
        preorder[1: firstIdxOfRightSubTree], postorder)
    postorderFromPreorderBST(
        preorder[firstIdxOfRightSubTree:], postorder)
    postorder.append(preorder[0])


preorder = [40, 30, 32, 35, 80, 90, 100, 120]
postorder = []
postorderFromPreorderBST(preorder, postorder)
print(postorder)
correctPostorder = [35, 32, 30, 120, 100, 90, 80, 40]
if postorder == correctPostorder:
    print('Correct')
