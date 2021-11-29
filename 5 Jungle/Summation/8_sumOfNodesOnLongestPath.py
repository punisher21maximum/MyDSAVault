

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

# O(n)

    def sumOfNodesOnLongestPath(self, currentPathRunningSum=0, currentPathRunningLength=0,
                                longestPathLength=0, longestPathSum=0):

        if not self:
            return

        currentPathRunningSum += self.value
        currentPathRunningLength += 1

        if self.left:
            longestPathLength, longestPathSum = self.left.sumOfNodesOnLongestPath(
                currentPathRunningSum, currentPathRunningLength,
                longestPathLength, longestPathSum
            )

        if self.right:
            longestPathLength, longestPathSum = self.right.sumOfNodesOnLongestPath(
                currentPathRunningSum, currentPathRunningLength,
                longestPathLength, longestPathSum
            )

        if self.left is None and self.right is None:

            if currentPathRunningLength > longestPathLength:
                longestPathSum = currentPathRunningSum
                longestPathLength = currentPathRunningLength
            if currentPathRunningLength == longestPathLength:
                longestPathSum = max(currentPathRunningSum, longestPathSum)
            print(self.value, longestPathSum)

        return longestPathLength, longestPathSum


if __name__ == "__main__":

    root = BT()
    for i in range(1, 16):
        root.insert(i)

    root.printTree()
    print()

    print(root.sumOfNodesOnLongestPath())
