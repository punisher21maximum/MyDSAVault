

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

    def sumOfAllParentNodesWithChildX(self, X):
        if not self:
            return 0

        if self.left:
            self.left.sumOfAllParentNodesWithChildX(X)

        if self.left and self.left.value == X:
            BT.sumOfNodes += self.value
        elif self.right and self.right.value == X:
            BT.sumOfNodes += self.value

        if self.right:
            self.right.sumOfAllParentNodesWithChildX(X)

        return BT.sumOfNodes

    def sumOfAllNodes2Iter(self, X):

        queue = [self]
        nodesSum = 0
        while queue:
            node = queue.pop(0)
            if node.left and node.left.value == X:
                nodesSum += node.value
            elif node.right and node.right.value == X:
                nodesSum += node.value

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


if __name__ == "__main__":

    root = BT()

    for i in range(1, 11):
        root.insert(i)

    root.printTree()

    print(root.sumOfAllNodes())
    print(root.sumOfAllNodes2Iter())
