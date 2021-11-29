

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

        queue = [self]
        while queue:
            node = queue.pop(0)
            print(node.value, end=' ')

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        print()

    def maxSumPathSum(self, runningSum=0, maxSumSoFar=0):

        if not self:
            return

        runningSum += self.value

        if self.left:
            maxSumSoFar = self.left.maxSumPathSum(
                runningSum, max(runningSum, maxSumSoFar))

        if self.right:
            maxSumSoFar = self.right.maxSumPathSum(
                runningSum, max(runningSum, maxSumSoFar))

        # print(max(runningSum, maxSumSoFar))
        return max(runningSum, maxSumSoFar)


if __name__ == "__main__":

    root = BT()
    for i in range(1, 16):
        root.insert(i)

    # root.printTree()
    print()

    print(root.maxSumPathSum())
