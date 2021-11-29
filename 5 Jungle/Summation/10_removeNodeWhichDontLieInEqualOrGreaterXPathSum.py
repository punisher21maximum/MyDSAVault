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

    def removeNodeWhichDontLieInPathWithPathSumEqualOrGreaterThanX(self, pathSumX, prevNode=None,
                                                                   runningSum=0):
        if not self:
            return

        runningSum += self.value

        if self.left:
            self.left.removeNodeWhichDontLieInPathWithPathSumEqualOrGreaterThanX(
                pathSumX, self, runningSum)

        if self.right:
            self.right.removeNodeWhichDontLieInPathWithPathSumEqualOrGreaterThanX(
                pathSumX, self, runningSum
            )

        if not self.left and not self.right and runningSum < pathSumX:
            print(self.value)
            if not prevNode:
                self = None
            else:
                if prevNode.left == self:
                    prevNode.left = None
                else:
                    prevNode.right = None


if __name__ == "__main__":

    root = BT()
    for i in range(1, 16):
        root.insert(i)

    root.printTree()
    print()

    root.removeNodeWhichDontLieInPathWithPathSumEqualOrGreaterThanX(20)

    root.printTree()
