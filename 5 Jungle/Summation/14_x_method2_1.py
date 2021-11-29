

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


def getMaxSumOfNodesWithNoNodesAdjacentHelper(node):
    if not node:
        summ = [0, 0]
        return summ

    leftSum = getMaxSumOfNodesWithNoNodesAdjacentHelper(node.left)
    rightSum = getMaxSumOfNodesWithNoNodesAdjacentHelper(node.right)

    summ = [0, 0]

    summ[0] = node.value + leftSum[1] + rightSum[1]

    summ[1] = (max(leftSum[0], leftSum[1]) +
               max(rightSum[0], rightSum[1]))

    return summ


def getMaxSumOfNodesWithNoNodesAdjacent(root):
    if not root:
        return 0

    # summ = [sum including current node, sum excluding current node]

    result = getMaxSumOfNodesWithNoNodesAdjacentHelper(root)
    return max(result[0], result[1])

# codeEnd


def printStack(arr):
    k = []
    for a in arr:
        k.append(a.value)
    return k


if __name__ == "__main__":

    root = BT()
    nodes = list(range(1, 16))
    # nodes = [10, -2, 7, 8, -4]
    for n in nodes:
        root.insert(n)
    # root = BT(1)
    # root.left = BT(2)
    # root.right = BT(3)
    # root.right.left = BT(4)
    # root.right.right = BT(5)
    # root.left.left = BT(1)

    root.printTree()
    print()

    print(getMaxSumOfNodesWithNoNodesAdjacent(root))
