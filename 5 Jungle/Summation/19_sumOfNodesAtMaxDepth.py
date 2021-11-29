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

    def mainFunc(self, node, level=0, maxDepth=float('-inf'), summ=0):
        '''
        Ques:
        Sum of nodes at maximum depth

        Thoery:
        At max depth we have leaves.
        So we keep track of the "level",
        "maxDepth" which is max level.

        When we reach leaves we check if
        depth GT maxDepth, we update maxDepth
        and summ = curr, if depth < maxDepth 
        then nohting and if depth == maxDepth
        we add to summ.
        '''
        if not node:
            return summ, maxDepth

        leftSum, leftMaxDepth = self.mainFunc(
            node.left, level+1, maxDepth, summ)
        rightSum, rightMaxDepth = self.mainFunc(
            node.right, level+1, maxDepth, summ)

        if leftMaxDepth > rightMaxDepth:
            maxDepth = leftMaxDepth
            summ = leftSum
        elif rightMaxDepth > leftMaxDepth:
            maxDepth = rightMaxDepth
            summ = rightSum
        else:
            maxDepth = leftMaxDepth
            summ = leftSum + rightSum

        if self.isLeaf(node):
            if level > maxDepth:
                maxDepth = level
                summ = node.value
            elif level == maxDepth:
                summ += node.value

        print(node.value, summ, maxDepth)

        return (summ, maxDepth)


if __name__ == "__main__":

    root = BT()
    for i in range(1, 8):
        root.insert(i)

    root.printTree()
    print()

    print(root.mainFunc(root))
