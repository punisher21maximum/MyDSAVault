from collections import defaultdict
from functools import reduce


class BT:

    sumOfNodes = 0

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.sumOfNodes = 0

    def insert(self, value):

        if not self.value:
            self.value = value
            return

        queue = [self]
        while queue:
            node = queue.pop(0)

            if not node.left:
                node.left = BT(value)
                break
            else:
                queue.append(node.left)

            if not node.right:
                node.right = BT(value)
                break
            else:
                queue.append(node.right)

    def printTree(self):

        queue = [self, None]
        while len(queue) > 1:
            node = queue.pop(0)

            if not node:
                print()
                queue.append(None)
                continue

            print(node.value, end=' ')

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        print()

    def isLeaf(self, node):

        return (not node.left and not node.right)

    def mainFunc(self, node, maxSum=0):
        '''
        Ques:
        Max subtree sum.

        Thoery:
        iterative solution - 
        take sum of alternate levels, return max



        '''
        if not node:
            return 0, 0

        leftSum, rightSum = 0, 0

        if self.left:
            leftSum, maxSum = self.mainFunc(node.left, maxSum)
        if self.right:
            rightSum, maxSum = self.mainFunc(node.right, maxSum)

        currSum = node.value + leftSum + rightSum
        print(node.value, currSum, max(currSum, maxSum))

        return (currSum, max(currSum, maxSum))


if __name__ == "__main__":

    root = BT(1)
    root.left = BT(-2)
    root.right = BT(3)
    root.left.left = BT(4)
    root.left.right = BT(5)
    root.right.left = BT(-6)
    root.right.right = BT(2)

    root.printTree()
    print()

    root.mainFunc(root)
