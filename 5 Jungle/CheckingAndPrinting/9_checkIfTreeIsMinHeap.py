

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

    def checkIfTreeIsMinHeap(self):
        if not self:
            return

        if self.left:
            if not self.left.checkIfTreeIsMinHeap():
                return False
        if self.right:
            if not self.right.checkIfTreeIsMinHeap():
                return False

        if self.left:
            if self.value > self.left.value:
                return False

        if self.right:
            if self.value > self.right.value:
                return False

        return True


if __name__ == "__main__":

    root = BT(11)
    # nodes = [10, 8, 2, 3, 5, 2]
    # nodes = [10, 8, 2, 3, 5, 2, 0, 1, 2, 2, 3, 1, 1, 0, 3]
    nodes = list(range(1, 16))
    for i in nodes:
        root.insert(i)

    root.printTree()
    print()

    print(root.checkIfTreeIsMinHeap())
