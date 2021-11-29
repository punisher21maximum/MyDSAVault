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

    def mainFunc(self, node, X, count=0):
        '''
        Ques:
        Subtree with given sum

        Thoery:
        To find the sum of subtree,
        summ = node + leftSubtree + rightSubtree

        So each node return the sum of
        subtree, rooted by itself

        None node returns 0 

        Leaf returns its own value

        We use DFS, so we get sum subtree
        wise, starting from bottom
        '''
        if not node:
            return 0, count

        ls, count = self.mainFunc(node.left, X, count)
        rs, count = self.mainFunc(node.right, X, count)

        summ = ls + node.value + rs
        print('>', node.value, summ)
        count = count + 1 if summ == X else count

        return (summ, count)


if __name__ == "__main__":

    root = BT(5)
    root.left = BT(-10)
    root.right = BT(3)
    root.left.left = BT(9)
    root.left.right = BT(8)
    root.right.left = BT(-4)
    root.right.right = BT(7)

    root.printTree()
    print()

    print(root.mainFunc(root, 7))
