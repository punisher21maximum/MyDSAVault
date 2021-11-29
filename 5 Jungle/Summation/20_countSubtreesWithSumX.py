

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


def countSubtreesWithSumX(root, givenSubtreeSum, count=0):
    if not root:
        return 0, count

    sumOfLeftSubtree, count = countSubtreesWithSumX(
        root.left, givenSubtreeSum, count)
    sumOfRightSubtree, count = countSubtreesWithSumX(
        root.right, givenSubtreeSum, count)

    sumOfCurrentSubtree = root.value + sumOfLeftSubtree + sumOfRightSubtree

    print(root.value, sumOfCurrentSubtree)

    if sumOfCurrentSubtree == givenSubtreeSum:
        count += 1
        print('Yes', root.value)

    return sumOfCurrentSubtree, count


# codeEnd


def printPath(path, idx):

    for i in range(idx, len(path)):
        print(path[i])


if __name__ == "__main__":

    # root = BT()
    # nodes = list(range(7, 0, -1))
    # # nodes = [1, -2, 3, 4, 5, -6, 2]
    # for n in nodes:
    #     root.insert(n)
    root = BT(5)
    root.left = BT(-10)
    root.right = BT(3)
    root.left.left = BT(9)
    root.left.right = BT(8)
    root.right.left = BT(-4)
    root.right.right = BT(7)

    givenSubtreeSum = 7
    print(countSubtreesWithSumX(root, givenSubtreeSum))
