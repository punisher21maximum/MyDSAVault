# 13_checkIfBTisCompleteBT.py


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

    def checkIfBTisCompleteBT(self, currentDepth=0, allowedLeafDepth=0):
        if not self:
            return True

        if self.left:
            result, allowedLeafDepth = self.left.checkIfBTisCompleteBT(
                currentDepth+1, allowedLeafDepth)
            if not result:
                return False, allowedLeafDepth
        if self.right:
            result, allowedLeafDepth = self.right.checkIfBTisCompleteBT(
                currentDepth+1, allowedLeafDepth)
            if not result:
                return False, allowedLeafDepth
        print(self.value, currentDepth, allowedLeafDepth)
        if not self.left and not self.right:
            print(self.value, currentDepth, allowedLeafDepth)
            if not allowedLeafDepth:
                allowedLeafDepth = currentDepth
            elif allowedLeafDepth != currentDepth:
                if allowedLeafDepth - 1 == currentDepth:
                    allowedLeafDepth -= 1
                    print(self.value, currentDepth, allowedLeafDepth)
                    return True, allowedLeafDepth
                else:
                    print(self.value, currentDepth, allowedLeafDepth)
                    return False, allowedLeafDepth
            else:
                return True, allowedLeafDepth

        if ((self.left and not self.right)
                or (not self.left and self.right)):
            return False, allowedLeafDepth

        return True, allowedLeafDepth

    def checkIfBTisCompleteBTIter(self):
        if not self:
            return True

        queue = [self]
        level = 0
        while queue:
            level += 1
            levelLength = len(queue)

            for i in range(levelLength):
                node = queue.pop()


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


if __name__ == "__main__":

    root = BT()
    # nodes = [10, 8, 2, 3, 5, 2]
    # nodes = [10, 8, 2, 3, 5, 2, 0, 1, 2, 2, 3, 1, 1, 0, 3]
    nodes = list(range(1, 16))
    for i in nodes:
        root.insert(i)

    temp = root
    while temp.left:
        temp = temp.left
    # print(temp.value)
    temp.left = BT(99)

    root.printTree()
    print()

    print(root.checkIfBTisCompleteBT())
