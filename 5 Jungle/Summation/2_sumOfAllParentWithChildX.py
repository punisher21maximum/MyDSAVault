

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

    def sumOfAllParentsWithChildXRecur(self, x, parentsSum=0):
        if not self:
            return 0

        parentsSum = 0

        if ((self.left and self.left.value == x) or
                (self.right and self.right.value == x)):
            parentsSum += self.value

        if self.left:
            parentsSum += self.left.sumOfAllParentsWithChildXRecur(
                x, parentsSum)
        if self.right:
            parentsSum += self.right.sumOfAllParentsWithChildXRecur(
                x, parentsSum)

        return parentsSum

    def sumOfAllParentsWithChildX(self, x):

        queue = [self]
        parentsSum = 0
        while queue:
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
                if node.left.value == x:
                    parentsSum += node.value

            if node.right:
                queue.append(node.right)
                if node.right.value == x:
                    parentsSum += node.value

        return parentsSum


if __name__ == "__main__":

    root = BT(4)
    root.left = BT(2)
    root.right = BT(5)
    root.left.left = BT(7)
    root.left.right = BT(2)
    root.right.left = BT(2)
    root.right.right = BT(3)

    root.printTree()

    print(root.sumOfAllParentsWithChildXRecur(2))
    # print(root.sumOfAllParentsWithChildX(2))
