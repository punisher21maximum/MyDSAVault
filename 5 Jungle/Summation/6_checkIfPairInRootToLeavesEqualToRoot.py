

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

    def sumOfLeftLeavesRecur(self):
        if not self:
            return 0

        leftLeavesSum = 0

        if self.left:
            leftNode = self.left
            if leftNode.left == None and leftNode.right == None:
                leftLeafNode = leftNode
                leftLeavesSum += leftLeafNode.value
            else:
                leftLeavesSum += self.left.sumOfLeftLeavesRecur()

        if self.right:
            leftLeavesSum += self.right.sumOfLeftLeavesRecur()

        return leftLeavesSum

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

    def checkIfPairInRootToLeavesEqualToRoot(self, rootValue, visitedPath=[]):

        if not self:
            return

        for prevNode in visitedPath:
            if self.left:
                leftValue = self.left.value
                if leftValue + prevNode == rootValue:
                    print('found', leftValue, prevNode)
                    return [leftValue, prevNode]
            if self.right:
                rightValue = self.right.value
                if rightValue + prevNode == rootValue:
                    print('found-', rightValue, prevNode)
                    return [leftValue, prevNode]

        if self.left:
            result = self.left.checkIfPairInRootToLeavesEqualToRoot(
                rootValue, visitedPath + [self.left.value])
            if result != False:
                return result

        if self.right:
            result = self.right.checkIfPairInRootToLeavesEqualToRoot(
                rootValue, visitedPath + [self.right.value])
            if result != False:
                return result

        return False

    def checkIfPairInRootToLeavesEqualToRootWithHashTable(self, rootValue, visitedNodes=[]):

        if not self:
            return

        currentValue = self.value
        remainingValue = rootValue - currentValue
        if remainingValue in visitedNodes:
            print(remainingValue, currentValue, visitedNodes)
            return True

        visitedNodes.append(currentValue)

        result = False
        if self.left:
            if self.left.checkIfPairInRootToLeavesEqualToRootWithHashTable(
                    rootValue, visitedNodes):
                return True

        if self.right:
            if self.right.checkIfPairInRootToLeavesEqualToRootWithHashTable(
                    rootValue, visitedNodes):
                return True

        return result


if __name__ == "__main__":

    root = BT()
    for i in range(1, 16):
        root.insert(i)

    root.printTree()
    print()

    # print(root.sumOfLeftLeavesRecur())
    for i in range(1, 50):
        print(i, root.checkIfPairInRootToLeavesEqualToRootWithHashTable(i))
