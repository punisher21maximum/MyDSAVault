from collections import defaultdict
from functools import reduce


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

        queue = [self, None]
        while len(queue) > 1:
            node = queue.pop(0)

            if not node:
                print()
                queue.append(None)
                continue

            print(node.value, end=' ')

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        print()

    def isLeaf(self, node):

        return (not node.left and not node.right)

    def mainFunc2(self, node, summ=0):
        '''
        Ques:
        Maximum sum of non adjacent levels.

        Thoery:
        iterative solution - 
        take sum of alternate levels, return max



        '''
        if not node:
            return 0

        if node.left:
            leftNode = node.left
            if leftNode.left:
                summ += self.mainFunc2(leftNode.left)
            if leftNode.right:
                summ += self.mainFunc2(leftNode.right)

        if node.right:
            rightNode = node.right
            if rightNode.left:
                summ += self.mainFunc2(rightNode.left)
            if rightNode.right:
                summ += self.mainFunc2(rightNode.right)

        return node.value + summ

    def mainFunc(self):

        sumOfOddLevel = self.mainFunc2(self)

        sumOfEvenLevel = (self.mainFunc2(self.left) +
                          self.mainFunc2(self.right))

        print(abs(sumOfOddLevel - sumOfEvenLevel))


if __name__ == "__main__":

    root = BT(5)
    root.left = BT(2)
    root.right = BT(6)
    root.left.left = BT(1)
    root.left.right = BT(4)
    root.left.right.left = BT(3)
    root.right.right = BT(8)
    root.right.right.right = BT(9)
    root.right.right.left = BT(7)

    root.printTree()
    print()

    root.mainFunc()
