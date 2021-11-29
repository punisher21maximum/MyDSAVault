

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
'''
 
'''


def printAllKSumPaths(root, k, path=[]):
    if not root:
        return

    path.append(root.value)

    printAllKSumPaths(root.left, k, path)
    printAllKSumPaths(root.right, k, path)

    sumOfPath = 0
    for i in reversed(range(len(path))):
        sumOfPath += path[i]

        if sumOfPath == k:
            print(path[i:])

    path.pop()


# codeEnd


def printPath(path, idx):

    for i in range(idx, len(path)):
        print(path[i])


if __name__ == "__main__":

    root = BT()
    # nodes = list(range(1, 8))
    # # nodes = [1, -2, 3, 4, 5, -6, 2]
    # for n in nodes:
    #     root.insert(n)
    root = BT(1)
    root.left = BT(3)
    root.left.left = BT(2)
    root.left.right = BT(1)
    root.left.right.left = BT(1)
    root.right = BT(-1)
    root.right.left = BT(4)
    root.right.left.left = BT(1)
    root.right.left.right = BT(2)
    root.right.right = BT(5)
    root.right.right.right = BT(2)

    root.printTree()
    print()
    k = 5
    print(printAllKSumPaths(root, k))
