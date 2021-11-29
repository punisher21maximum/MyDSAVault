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

    def mainFunc(self, node, currMaxSumOfNodeToLeafPath=0):
        '''
        Ques:
        Find the maximum sum leaf to root path 

        Thoery:
        For every node we have to find, the max
        sum path from currNode to any leaf rooted 
        by this node.

        So at every node, we find max sum path
        from leaf to node, maxSum = nodeVal + (
            leftMaxSum + rightMaxSum
        )

        '''
        if not node:
            return 0

        leftMaxSumOfNodeToLeafPath = self.mainFunc(node.left)
        rightMaxSumOfNodeToLeafPath = self.mainFunc(node.right)

        currMaxSumOfNodeToLeafPath = node.value + max(
            leftMaxSumOfNodeToLeafPath,
            rightMaxSumOfNodeToLeafPath
        )

        print(node.value, currMaxSumOfNodeToLeafPath)

        return currMaxSumOfNodeToLeafPath


if __name__ == "__main__":

    root = BT(10)
    root.left = BT(-2)
    root.right = BT(7)
    root.left.left = BT(8)
    root.left.right = BT(-4)
    # for i in range(1, 14):
    #     root.insert(i)

root.printTree()
print()

print(root.mainFunc(root))
