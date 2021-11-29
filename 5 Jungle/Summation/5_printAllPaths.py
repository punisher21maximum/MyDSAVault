

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

# all paths

    def printAllPaths(self, visitedPath=[]):

        if not self:
            return

        if self.left:
            self.left.printAllPaths(
                visitedPath + [self.left.value])

        if self.right:
            self.right.printAllPaths(
                visitedPath + [self.right.value])

        if self.left == None and self.right == None:
            print(visitedPath)


if __name__ == "__main__":

    root = BT()
    for i in range(1, 16):
        root.insert(i)

    # root.printTree()
    print()

    root.printAllPaths()
