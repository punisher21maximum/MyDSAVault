

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

    def convertBTToSumTree(self, node, summ=0):
        '''
        Convert this to a tree where each node 
        contains the sum of the left and right 
        sub trees in the original tree.
        '''
        if not node:
            return 0

        summ += self.convertBTToSumTree(node.left)
        summ += self.convertBTToSumTree(node.right)

        nodeVal = node.value
        node.value = summ
        summ += nodeVal

        return summ

    def convertBTToSumTreeTwo(self, node):
        if not node:
            return 0

        leftSum = self.convertBTToSumTreeTwo(node.left)
        rightSum = self.convertBTToSumTreeTwo(node.right)

        nodeVal = node.value
        node.value = leftSum + rightSum

        return nodeVal + leftSum + rightSum


if __name__ == '__main__':
    t = BT()
    t.root = Node(10)
    t.root.left = Node(-2)
    t.root.right = Node(6)
    t.root.left.left = Node(8)
    t.root.left.right = Node(-4)
    t.root.right.left = Node(7)
    t.root.right.right = Node(5)
    '''
in   8 4 9 2 10 5 1 6 3 7
pre  1 2 4 8 9 5 10 3 6 7
post 8 9 4 10 5 2 6 7 3 1
    '''

    t.BFSLevelOrderTraversal()
    print()
    t.convertBTToSumTree(t.root)
    print()
    t.convertBTToSumTreeTwo(t.root)
    print()
    t.BFSLevelOrderTraversal()
