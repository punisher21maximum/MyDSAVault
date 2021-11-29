

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

    def printSumOfTreeAtEachNodeAsRoot(self):
        if not self:
            return True

        runningSum = self.value

        if self.left:
            runningSum += self.left.printSumOfTreeAtEachNodeAsRoot()
        if self.right:
            runningSum += self.right.printSumOfTreeAtEachNodeAsRoot()

        print(self.value, runningSum)

        return runningSum


if __name__ == "__main__":

    root = BT()
    # nodes = [1, 2, 3, 4, 5]
    # nodes = [10, 8, 2, 3, 5, 2, 0, 1, 2, 2, 3, 1, 1, 0, 3]
    nodes = list(range(1, 16))
    for i in nodes:
        root.insert(i)

    root.printSumOfTreeAtEachNodeAsRoot()
    print()


'''
1. complete iter for 9
'''
