

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

#

    def checkSumOfUncoveredAndCoveredNodesIsSame(self):

        sumOfUncoveredNodes = self.getSumOfLeftUncoveredNodes() + \
            self.getSumOfRightUncoveredNodes()
        sumOfAllNodes = self.getSumOfCompleteTree()

        if sumOfAllNodes == sumOfUncoveredNodes * 2:
            return True
        else:
            return False

    def getSumOfCompleteTree(self):
        if not self:
            return

        sumOfAllNodes = self.value
        if self.left:
            sumOfAllNodes += self.left.getSumOfCompleteTree()
        if self.right:
            sumOfAllNodes += self.right.getSumOfCompleteTree()

        return sumOfAllNodes

    def getSumOfLeftUncoveredNodes(self):
        if not self:
            return 0

        if not self.left and not self.right:
            return self.value

        if self.left:
            return self.value + self.left.getSumOfLeftUncoveredNodes()
        else:
            return self.value + self.right.getSumOfLeftUncoveredNodes()

    def getSumOfLeftUncoveredNodes2(self):
        if not self:
            return 0

        summ = 0
        if not self.left and not self.right:
            summ += self.value

        if self.left:
            summ += self.value + self.left.getSumOfLeftUncoveredNodes2()
        else:
            summ += self.value + self.right.getSumOfLeftUncoveredNodes2()

        return summ

    def getSumOfRightUncoveredNodes(self):
        if not self:
            return 0

        sumOfLeftUncoveredNodes, sumOfRightUncoveredNodes = 0, 0
        node = self.left
        while True:
            while node.left:
                sumOfLeftUncoveredNodes += node.value
                node = node.left

            if node.right:
                node = node.right
            else:
                break

        node = self.right
        while True:
            while node.right:
                sumOfRightUncoveredNodes += node.value
                node = node.right

            if node.left:
                node = node.left
            else:
                break

        sumOfUncoveredNodes = sumOfLeftUncoveredNodes + \
            self.value + sumOfRightUncoveredNodes

        return sumOfUncoveredNodes


if __name__ == "__main__":

    root = BT()
    nodes = [1, 2, 3, 4, 5, 6, 7]
    # nodes = [10, 8, 2, 3, 5, 2, 0, 1, 2, 2, 3, 1, 1, 0, 3]
    # nodes = list(range(1, 16))
    for i in nodes:
        root.insert(i)

    root.printTree()
    print()

    print(root.getSumOfLeftUncoveredNodes2())
