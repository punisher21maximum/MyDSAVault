

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

    def sumOfMaximumLevelSum(self, currentLevel=0, maxLevelSum=0,
                             sumOfLevelsDict={}):
        if not self:
            return

        currentLevel += 1

        if currentLevel in sumOfLevelsDict:
            sumOfLevelsDict[currentLevel] += self.value
        else:
            sumOfLevelsDict[currentLevel] = self.value

        currentLevelSum = sumOfLevelsDict[currentLevel]
        maxLevelSum = max(currentLevelSum, maxLevelSum)

        if self.left:
            maxLevelSum = self.left.sumOfMaximumLevelSum(
                currentLevel, maxLevelSum, sumOfLevelsDict
            )

        if self.right:
            maxLevelSum = self.right.sumOfMaximumLevelSum(
                currentLevel, maxLevelSum, sumOfLevelsDict
            )

        return maxLevelSum

    def sumOfMaximumLevelSumIter(self):

        queue = [self]

        pass


if __name__ == "__main__":

    root = BT()
    for i in range(1, 16):
        root.insert(i)

    root.printTree()
    print()

    print(root.sumOfMaximumLevelSum())
