# 13_findMaxSumRootToLeafPathpy


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

    def findMaxSumRootToLeafPath(self, currentPathSum=0, maxSumFromPaths=float('-inf'), path=[]):
        if not self:
            return

        path.append(self.value)
        currentPathSum += self.value

        if not self.left and not self.right:
            maxSumFromPaths = max(currentPathSum, maxSumFromPaths)
            print(self.value, path, currentPathSum, maxSumFromPaths)

        if self.left:
            maxSumFromPaths = self.left.findMaxSumRootToLeafPath(
                currentPathSum, maxSumFromPaths, path)
        if self.right:
            maxSumFromPaths = self.right.findMaxSumRootToLeafPath(
                currentPathSum, maxSumFromPaths, path)

        path.pop()

        return maxSumFromPaths


def printStack(arr):
    k = []
    for a in arr:
        k.append(a.value)
    return k


if __name__ == "__main__":

    root = BT()
    nodes = list(range(7, 0, -1))
    nodes = [10, -2, 7, 8, -4]
    for n in nodes:
        root.insert(n)

    root.printTree()
    print()

    print(root.findMaxSumRootToLeafPath())
