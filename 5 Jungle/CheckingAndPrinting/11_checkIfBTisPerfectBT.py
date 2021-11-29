

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

    def checkIfBTisPerfectBT(self, currentDepth=0, leafDepth=0):
        if not self:
            return True

        if self.left:
            result, leafDepth = self.left.checkIfBTisPerfectBT(
                currentDepth+1, leafDepth)
            if not result:
                return False, leafDepth
        if self.right:
            result, leafDepth = self.right.checkIfBTisPerfectBT(
                currentDepth+1, leafDepth)
            if not result:
                return False, leafDepth

        print(self.value, currentDepth, leafDepth)
        if not self.left and not self.right:
            if not leafDepth:
                leafDepth = currentDepth
            elif leafDepth != currentDepth:
                return False, leafDepth
            else:
                return True, leafDepth

        if ((self.left and not self.right)
                or (not self.left and self.right)):
            return False, leafDepth

        return True, leafDepth

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


if __name__ == "__main__":

    root = BT()
    # nodes = [10, 8, 2, 3, 5, 2]
    # nodes = [10, 8, 2, 3, 5, 2, 0, 1, 2, 2, 3, 1, 1, 0, 3]
    nodes = list(range(1, 16))
    for i in nodes:
        root.insert(i)

    root.printTree()
    print()

    print(root.checkIfBTisPerfectBT())
