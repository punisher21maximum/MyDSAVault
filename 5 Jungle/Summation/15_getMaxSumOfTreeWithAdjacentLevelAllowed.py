

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
1. get sum of each level - in sumOfLevels
2. find max sum from sumOfLevels with no two level adjacent
'''


def getMaxFromArrayWithAdjacentNotAllowed(sumOfLevels):
    if not sumOfLevels:
        return 0

    maxSum = [0, 0]
    for i in range(len(sumOfLevels)):
        maxSum1 = max(maxSum[0], maxSum[1])
        maxSum[0] = sumOfLevels[i] + maxSum[1]
        maxSum[1] = maxSum1

    return max(maxSum[0], maxSum[1])


def getMaxSumOfTreeWithAdjacentLevelAllowedHelper(root):
    if not root:
        return 0

    sumOfLevels = []
    level = -1

    queue = [root]
    while queue:
        lengthOfLevel = len(queue)
        level += 1
        sumOfLevels.append(0)

        for _ in range(lengthOfLevel):
            node = queue.pop(0)

            sumOfLevels[level] += node.value

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return sumOfLevels


def getMaxSumOfTreeWithAdjacentLevelAllowed(root):
    if not root:
        return 0

    sumOfLevels = getMaxSumOfTreeWithAdjacentLevelAllowedHelper(root)
    return getMaxFromArrayWithAdjacentNotAllowed(sumOfLevels)


# codeEnd


def printStack(arr):
    k = []
    for a in arr:
        k.append(a.value)
    return k


if __name__ == "__main__":

    root = BT()
    # nodes = list(range(1, 16))
    nodes = [10, -2, 7, 8, -4]
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

    print(getMaxSumOfTreeWithAdjacentLevelAllowed(root))
