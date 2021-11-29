

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

    def sumOfSubtree(self, node):
        if not node:
            return 0

        return (self.sumOfSubtree(node.left) +
                node.value + self.sumOfSubtree(node.right))

    def checkIfSumTree(self, node):
        '''
        Sum Tree:
        Node.value = sum(leftSubtree.value + rightSubtree.value)
        Time: (n^2)
        '''
        if not node or not node.left or not node.right:
            return True

        leftSubtreeSum = self.sumOfSubtree(node.left)
        rightSubtreeSum = self.sumOfSubtree(node.right)

        return (node.value == (leftSubtreeSum + rightSubtreeSum) and
                self.checkIfSumTree(node.left) and self.checkIfSumTree(node.right))

    def checkIfSumTree2(self, node):
        '''
        Sum Tree:
        Node.value = sum(leftSubtree.value + rightSubtree.value)
        Time: (n^2)

        Note: to find the sum of leftsubtree/rightsubtree
        we do not have to recursively find the sum of children nodes.
        If the sumTree prop is True for children then 
        sum of leftSubtree = 2 * (value of left node)

        So 

        '''
        if not node or (not node.left and not node.right):
            return True

        if node.left:
            self.checkIfSumTree2(node.left)

        if node.right:
            self.checkIfSumTree2(node.right)

        leftSum, rightSum = 0, 0

        if not node.left:
            leftSum = 0
        elif not node.left.left and not node.left.right:
            leftSum = node.left.value
        else:
            leftSum = node.left.value * 2

        if not node.right:
            rightSum = 0
        elif not node.right.left and not node.right.right:
            rightSum = node.right.value
        else:
            rightSum = node.right.value * 2

        return node.value == (leftSum + rightSum)


if __name__ == '__main__':
    t = BT()
    root = t.root
    root = Node(26)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(3)
    t.root = root
    # vals = list(range(1, 16))
    # for i in vals:
    #     t.insert(i)
    '''
    in   8 4 9 2 10 5 1 6 3 7
    pre  1 2 4 8 9 5 10 3 6 7
    post 8 9 4 10 5 2 6 7 3 1
    '''

    t.BFSLevelOrderTraversal()
    print()
    print(t.checkIfSumTree2(t.root))
