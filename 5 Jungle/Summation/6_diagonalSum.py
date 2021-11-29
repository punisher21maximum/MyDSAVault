

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


# Non-optimal | O(n*n)


    def diagonalSumHelper(self, verticalDistance, diagonalSumDict):
        if not self:
            return

        if verticalDistance not in diagonalSumDict:
            diagonalSumDict[verticalDistance] = 0
        diagonalSumDict[verticalDistance] += self.value

        if self.left:
            self.left.diagonalSumHelper(verticalDistance + 1, diagonalSumDict)

        if self.right:
            self.right.diagonalSumHelper(verticalDistance, diagonalSumDict)

    def diagonalSum(self):

        diagonalSumDict = dict()
        self.diagonalSumHelper(0, diagonalSumDict)
        for key in diagonalSumDict:
            print(diagonalSumDict[key], end=' ')

# optimal | O(n)

    def diagonalSumHelper2(self, row, col, diagonalSumDict):
        if not self:
            return

        if row - col not in diagonalSumDict:
            diagonalSumDict[row - col] = 0
        diagonalSumDict[row - col] += self.value

        if self.left:
            self.left.diagonalSumHelper2(row + 1, col - 1, diagonalSumDict)

        if self.right:
            self.right.diagonalSumHelper2(row + 1, col + 1, diagonalSumDict)

    def diagonalSum2(self):

        diagonalSumDict = dict()

        self.diagonalSumHelper2(0, 0, diagonalSumDict)

        for diagonalSum in diagonalSumDict:
            print(diagonalSumDict[diagonalSum])

# solution 3

    def diagonalSumIterative(self):  # Time O(Nlog(N)) | Space O(N)
        if not self.root:
            return

        result = []
        summ = 0

        queue = [self.root]
        node = None
        while queue:
            if not node:
                node = queue.pop(0)
                print(sum)
                summ = 0

            result.append(node.value)
            summ += node.value

            if node.left:
                queue.append(node.left)

            node = node.right

        print(result)


if __name__ == "__main__":

    root = BT(1)
    root.left = BT(2)
    root.right = BT(3)
    root.left.left = BT(9)
    root.left.right = BT(6)
    root.right.left = BT(4)
    root.right.right = BT(5)
    root.right.left.right = BT(7)
    root.right.left.left = BT(12)
    root.left.right.left = BT(11)
    root.left.left.right = BT(10)

    root.printTree()

    # print(root.sumOfLeftLeavesRecur())
    print(root.diagonalSum2())
