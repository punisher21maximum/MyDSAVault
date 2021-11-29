

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


def sumOfNodesAtMaxDepth(root, currentLevel=0, maxDepthLevel=0, summ=0):
    if not root:
        return maxDepthLevel, summ

    maxDepthLevel, summ = sumOfNodesAtMaxDepth(
        root.left, currentLevel+1, maxDepthLevel, summ)
    maxDepthLevel, summ = sumOfNodesAtMaxDepth(
        root.right, currentLevel+1, maxDepthLevel, summ)

    if not root.left and not root.right:
        if maxDepthLevel == 0:
            maxDepthLevel = currentLevel
            summ += root.value
        elif currentLevel == maxDepthLevel:
            summ += root.value
        elif currentLevel > maxDepthLevel:
            maxDepthLevel = currentLevel
            summ = root.value

    print(root.value, maxDepthLevel, summ)

    return maxDepthLevel, summ


# codeEnd


def printPath(path, idx):

    for i in range(idx, len(path)):
        print(path[i])


if __name__ == "__main__":

    # root = BT()
    # nodes = list(range(1, 8))
    # # nodes = [1, -2, 3, 4, 5, -6, 2]
    # for n in nodes:
    #     root.insert(n)
    root = BT(5)
    root.left = BT(-10)
    root.right = BT(3)
    root.left.left = BT(9)
    root.left.right = BT(8)
    root.left.right.left = BT(2)
    root.right.left = BT(1)
    root.right.left.right = BT(9)
    root.right.right = BT(7)

    print(sumOfNodesAtMaxDepth(root))
