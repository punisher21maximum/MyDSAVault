def findAllPossibleBTFromInAndPrintPre(inorder, preorder, inden=''):

    if len(inorder) == 0:
        # print(preorder)
        return

    for i in range(len(inorder)):
        leftIn = inorder[:i]
        root = inorder[i]
        rightIn = inorder[i + 1:]
        # print(inden + 'r', root)

        print(inden + 'r', root)
        preorder.append(root)

        findAllPossibleBTFromInAndPrintPre(leftIn, preorder, inden + '----')
        findAllPossibleBTFromInAndPrintPre(rightIn, preorder, inden + '----')


inorder = [5, 6, 7]
preorder = []
findAllPossibleBTFromInAndPrintPre(inorder, preorder)
