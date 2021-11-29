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

    def mainFunc(self, node, X):
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
            return 0

        ls = self.mainFunc(node.left, X)
        rs = self.mainFunc(node.right, X)

        summ = ls + node.value + rs
        if summ == X:
            print('Found, root:', node.value)

        return summ


if __name__ == "__main__":

    root = BT()
    for i in range(1, 6):
        root.insert(i)

    root.printTree()
    print()

    print(root.mainFunc(root, 5))
