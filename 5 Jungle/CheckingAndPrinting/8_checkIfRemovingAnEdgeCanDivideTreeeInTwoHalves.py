

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

    def getCountOfTotalNodes(self):
        if not self:
            return 0

        countOfNodes = 0

        if self.left:
            countOfNodes += self.left.getCountOfTotalNodes()
        if self.right:
            countOfNodes += self.right.getCountOfTotalNodes()

        return countOfNodes + 1

    def checkIfRemovingAnEdgeCanDivideTreeInTwoHalvesHelper2(self, totalNodes):
        if not self:
            return False

        countOfNodes, result = 0, False

        if self.left:
            result, leftCount = self.left.checkIfRemovingAnEdgeCanDivideTreeInTwoHalvesHelper(
                totalNodes)
            if result:
                return True
            countOfNodes += leftCount

        if self.right:
            result, rightCount = self.right.checkIfRemovingAnEdgeCanDivideTreeInTwoHalvesHelper(
                totalNodes)
            if result:
                return True
            countOfNodes += rightCount

        countOfNodes += 1

        if countOfNodes * 2 == totalNodes:
            print(self.value, countOfNodes, totalNodes)
            result = True

        print('v', self.value, countOfNodes, totalNodes)
        return result, countOfNodes

    def checkIfRemovingAnEdgeCanDivideTreeInTwoHalvesHelper(self, totalNodes):
        if not self:
            return False

        if self.getCountOfTotalNodes() * 2 == totalNodes:
            print(self.value)
            return True

        if self.left:
            if self.left.checkIfRemovingAnEdgeCanDivideTreeInTwoHalvesHelper(
                    totalNodes):
                return True

        if self.right:
            if self.right.checkIfRemovingAnEdgeCanDivideTreeInTwoHalvesHelper(
                    totalNodes):
                return True

        return False

    def checkIfRemovingAnEdgeCanDivideTreeInTwoHalves(self):
        if not self:
            return False

        totalNodes = self.getCountOfTotalNodes()
        return self.checkIfRemovingAnEdgeCanDivideTreeInTwoHalvesHelper(totalNodes)


if __name__ == "__main__":

    root = BT()
    # nodes = [1, 2, 3, 4, 5]
    # nodes = [10, 8, 2, 3, 5, 2, 0, 1, 2, 2, 3, 1, 1, 0, 3]
    # nodes = list(range(1, 16))
    # for i in nodes:
    #     root.insert(i)
    root.value = 5
    root.left = BT(1)
    root.left.left = BT(3)
    root.left.right = BT(24)
    root.left.left.left = BT(13)
    root.left.left.right = BT(33)
    root.right = BT(6)
    root.right.left = BT(7)
    root.right.right = BT(4)
    root.right.left.left = BT(3)
    root.right.left.right = BT(2)
    root.right.right.right = BT(8)

    print(root.checkIfRemovingAnEdgeCanDivideTreeInTwoHalves())

    print()
