

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

# solution 1: Time O(n^2)
    def constructTreeFromInorderAndPreorder(self, inorder,
                                            preorder):
        '''
        Find root, leftSubtree and rightSubtree 
        Function return root for a given inorder and preorder recursively 
        We can take preorder[0] as root 
        and root of leftSubtree as leftnode 
        and root of rightSubtree as rightnode 

        At last function return root of tree
        which is assigned to the object of class -> t.root = func(in, pre)
        '''
        if not preorder:
            return

        rootVal = preorder[0]
        node = Node(rootVal)
        for idx in range(len(inorder)):
            if inorder[idx] == rootVal:
                rootIdx = idx
                break

        lenOfLeftSubtree = len(inorder[:rootIdx])
        node.left = self.constructTreeFromInorderAndPreorder(
            inorder[:rootIdx], preorder[1:lenOfLeftSubtree + 1])

        node.right = self.constructTreeFromInorderAndPreorder(
            inorder[rootIdx + 1:], preorder[lenOfLeftSubtree + 1:])

        return node

# solution 2: Time O(n)
    def constructTreeFromInorderAndPreorderTwo(self, inorder, preorder):
        '''
        Solution 1 is O(n^2), because searching for index
        of root in inorder takes O(n) time.
        Using hash table we can make search in O(1) time.
        So final solution will be O(n)

        hashTable = dict()
        for idx in range(len(inorder)):
            hashTable[idx] = inorder[idx]
        '''
        pass


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

    inorder = ['D', 'B', 'E', 'A', 'F', 'C']
    preorder = ['A', 'B', 'D', 'E', 'C', 'F']
    t.root = t.constructTreeFromInorderAndPreorder(inorder, preorder)
    print()
    t.BFSLevelOrderTraversal()
