

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BT:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)

        if not self.root:
            self.root = newNode
            return

        queue = [self.root]
        while queue:
            currentNode = queue.pop(0)

            if not currentNode.left:
                currentNode.left = newNode
                return
            else:
                queue.append(currentNode.left)

            if not currentNode.right:
                currentNode.right = newNode
                return
            else:
                queue.append(currentNode.right)

    def BFSLevelOrderTraversal(self):
        if not self.root:
            return

        queue = [self.root]
        while queue:
            currentNode = queue.pop(0)

            print(currentNode.value, end=' ')

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

        return False

    def printInorder(self, node):
        if not node:
            return

        if node.left:
            self.printInorder(node.left)

        print(node.value, end=' ')

        if node.right:
            self.printInorder(node.right)

    def getRootIdx(self, inorder, rootVal):

        for idx in range(len(inorder)):
            if inorder[idx] == rootVal:
                return idx
        return None

# solution 1: Time O(n^3)
    def constructTreeFromInorderAndLevelorder(self, levelorder,
                                              inorder):
        '''
        Find root, leftSubtree and rightSubtree 
        Function return root for a given levelorder and inorder recursively 
        We can take levelorder[0] as root 
        and root of leftSubtree as leftnode 
        and root of rightSubtree as rightnode 

        At last function return root of tree
        which is assigned to the object of class -> t.root = func(level, in)
        '''
        if not inorder:
            return

        rootVal = levelorder[0]
        node = Node(rootVal)
        print(rootVal, inorder, levelorder)
        for idx in range(len(inorder)):
            if inorder[idx] == rootVal:
                rootIdx = idx
                break

        inorderLeft, inorderRight = inorder[:rootIdx], inorder[rootIdx+1:]
        levelorderLeft, levelorderRight = [], []
        for i in range(1, len(levelorder)):
            if levelorder[i] in inorderLeft:
                levelorderLeft.append(levelorder[i])
            else:
                levelorderRight.append(levelorder[i])

        node.left = self.constructTreeFromInorderAndLevelorder(
            levelorderLeft, inorderLeft)

        node.right = self.constructTreeFromInorderAndLevelorder(
            levelorderRight, inorderRight)

        return node

# solution 2: Time O(n^3)
    def constructTreeFromInorderAndLevelorderTwo(self, levelorder,
                                                 inorder):
        '''
        Solution 1 is O(n^3) 
        As we have to find levelorderLeft and levelorderRight subtrees 
        We can use levelorderIndex instead to get
        O(n) solution
        '''
        if not inorder:
            return

        for levelorderIdx in range(len(levelorder)):
            levelEle = levelorder[levelorderIdx]

            for inorderIdx in range(len(inorder)):
                inorderEle = inorder[inorderIdx]

                rootVal = levelEle  # or inorderEle
                if levelEle == inorderEle:
                    node = Node(rootVal)

                rootIdx = inorderIdx

                break

        node.left = self.constructTreeFromInorderAndLevelorderTwo(levelorder,
                                                                  inorder[:rootIdx])
        node.right = self.constructTreeFromInorderAndLevelorderTwo(levelorder,
                                                                   inorder[rootIdx + 1:])

        return node


if __name__ == '__main__':
    t = BT()
    vals = list(range(1, 11))
    # for i in vals:
    #     t.insert(i)
    '''
in   8 4 9 2 10 5 1 6 3 7
pre  1 2 4 8 9 5 10 3 6 7
post 8 9 4 10 5 2 6 7 3 1
    '''

    levelorder = [20, 8, 22, 4, 12, 10, 14]
    inorder = [4, 8, 10, 12, 14, 20, 22]
    t.root = t.constructTreeFromInorderAndLevelorderTwo(
        levelorder, inorder)
    print()
    t.printInorder(t.root)
