# maxSpiralSumInBT


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


def maxSpiralSumInBT(root):
    if not root:
        return

    queue = [root]
    level = 0
    spiralOrder = []

    while queue:

        sizeOfCurrentLevel = len(queue)
        level += 1
        print('level:', level, 'val:', end=' ')

        for i in range(sizeOfCurrentLevel):

            if level % 2 != 0:  # odd
                node = queue.pop(-1)
                print(node.value, end=' ')

                spiralOrder.append(node.value)

                if node.right:
                    queue.insert(0, node.right)
                if node.left:
                    queue.insert(0, node.left)

            else:
                node = queue.pop(0)
                print(node.value, end=' ')

                spiralOrder.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        print()
        printQ(queue)

    return spiralOrder


def maxSubarraySum(array):

    currSum = array[0]
    maxSum = array[0]

    for i in range(1, len(array)):
        currSum = max(currSum + array[i], array[i])
        maxSum = max(currSum, maxSum)

    return maxSum


# codeEnd


def printQ(q):
    for i in q:
        print(i.value, end=' ')
    print()


if __name__ == "__main__":

    # root = BT()
    # nodes = list(range(1, 16))
    # # nodes = [1, -2, 3, 4, 5, -6, 2]
    # for n in nodes:
    #     root.insert(n)
    root = BT(-2)
    root.left = BT(-3)
    root.right = BT(4)
    root.left.left = BT(5)
    root.left.right = BT(1)
    root.right.left = BT(-2)
    root.right.right = BT(-1)
    root.left.left.left = BT(-3)
    root.right.right.right = BT(2)

    print(maxSpiralSumInBT(root))
