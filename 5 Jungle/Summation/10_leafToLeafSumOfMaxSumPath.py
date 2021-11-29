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

    def mainFunc(self, node, currSumOfMaxSumLeafToLeafPath=0):
        '''
        Ques:
        for leaf to leaf path, find maxSum path

        Thoery:
        At every node, except leaf node, for path
        from that node to every leaf on its left,
        we find the maxSum path, and same for right
        subtree.
        We have to include the current node to 
        complete the path.

        So at current node we have three values,
        maxSumLeafToLeafPath from leftSubtree,
        from rightSubtree and including currNode.

        We return two things, one is a SumOfMaxSumPath
        from currentNode to leaf, and SumOfmaxSumLeafToLeafPath

        '''
        if not node:
            return 0, 0

        if self.isLeaf(node):
            return 0, node.value

        leftSumOfMaxSumLeafToLeafPath, leftSumOfMaxSumNodeToLeafPath = self.mainFunc(
            node.left, currSumOfMaxSumLeafToLeafPath
        )

        rightSumOfMaxSumLeafToLeafPath, rightSumOfMaxSumNodeToLeafPath = self.mainFunc(
            node.right, currSumOfMaxSumLeafToLeafPath
        )

        if node.left and node.right:
            currSumOfMaxSumLeafToLeafPath = max(
                leftSumOfMaxSumLeafToLeafPath,
                rightSumOfMaxSumLeafToLeafPath,
                leftSumOfMaxSumNodeToLeafPath + node.value + rightSumOfMaxSumNodeToLeafPath
            )
        else:
            currSumOfMaxSumLeafToLeafPath = max(
                leftSumOfMaxSumLeafToLeafPath,
                rightSumOfMaxSumLeafToLeafPath
            )

        currSumOfMaxSumNodeToLeafPath = node.value + max(
            leftSumOfMaxSumNodeToLeafPath,
            rightSumOfMaxSumNodeToLeafPath
        )

        print(node.value, currSumOfMaxSumLeafToLeafPath,
              currSumOfMaxSumNodeToLeafPath)

        return currSumOfMaxSumLeafToLeafPath, currSumOfMaxSumNodeToLeafPath


if __name__ == "__main__":

    root = BT(-15)
    root.left = BT(5)
    root.right = BT(6)
    root.left.left = BT(-8)
    root.left.right = BT(1)
    root.left.left.left = BT(2)
    root.left.left.right = BT(6)
    root.right.left = BT(3)
    root.right.right = BT(9)
    root.right.right.right = BT(0)
    root.right.right.right.left = BT(4)
    root.right.right.right.right = BT(-1)
    root.right.right.right.right.left = BT(10)
    # for i in range(1, 14):
    #     root.insert(i)

    root.printTree()
    print()

    print(root.mainFunc(root))
