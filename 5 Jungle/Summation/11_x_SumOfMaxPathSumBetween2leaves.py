# 10_removeNodeWhichDontLieInEqualOrGreaterXPathSum


class BT:

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

        queue = [self]
        while queue:
            node = queue.pop(0)
            print(node.value, end=' ')

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        print()

# Code

    def SumOfMaxPathSumBetween2leaves(self, maxBranchSum=0, maxPathSum=0):
        if not self:
            return

        leftMaxSumBranch, rightMaxSumBranch = 0, 0
        leftMaxPathSum, rightMaxPathSum = 0, 0

        if self.left:
            leftMaxSumBranch, leftMaxPathSum = self.left.SumOfMaxPathSumBetween2leaves(
                maxBranchSum, maxPathSum
            )

        if self.right:
            rightMaxSumBranch, rightMaxPathSum = self.right.SumOfMaxPathSumBetween2leaves(
                maxBranchSum, maxPathSum
            )

        maxSumAsBranch = self.value + max(leftMaxSumBranch, rightMaxSumBranch)

        maxPathSum = max(
            leftMaxPathSum, rightMaxPathSum,
            leftMaxSumBranch + self.value + rightMaxSumBranch
        )

        return maxSumAsBranch, maxPathSum


if __name__ == "__main__":

    root = BT(1)
    root.insert(1000)
    for i in range(1, 16):
        root.insert(i)
    root.insert(2000)

    root.printTree()
    print()

    print(root.SumOfMaxPathSumBetween2leaves())
