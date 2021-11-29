#  printMiddleLevelOfPerfectBT


class BT:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

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

    def func(self, d=0):
        if not self:
            return self

        if self.left:
            self.left.func(d+1)
        if self.right:
            self.right.func(d+1)

        print(self.value, d)

    def func2(self, d=0, maxD=0):
        if not self:
            return self

        if self.left:
            maxD = self.left.func2(d+1)
        if self.right:
            maxD = self.right.func2(d+1)

        maxD = max(d, maxD)
        print(self.value, d, maxD)

        return maxD

    def func3(self, d=0, maxD=0):
        if not self:
            return self

        if self.left:
            maxD = self.left.func3(d+1, maxD)
        if self.right:
            maxD = self.right.func3(d+1, maxD)

        maxD = max(d, maxD)
        print(self.value, d, maxD)

        return maxD


# code


def printMiddleLevelOfPerfectBT(slowPtr, fastPtr):
    if not fastPtr:
        return


def printQ(q):
    print('-> ', end='')
    for n in q:
        print(n.value, end=' ')
    print()


if __name__ == "__main__":

    root1 = BT(5)
    root1.left = BT(2)
    root1.right = BT(3)
    root1.left.left = BT(1)
    root1.left.right = BT(4)
    root1.left.right.left = BT(6)
    root1.left.right.right = BT(8)

    root1.printTree()
    print()

    sequence = [5, 2, 4, 8]
    print(printMiddleLevelOfPerfectBT(root1, root1))
