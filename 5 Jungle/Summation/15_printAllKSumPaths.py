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

    def mainFunc(self, node, K, path=[]):
        '''
        Ques:
        All K sum paths, from any node to
        any node. All downward paths.

        Thoery:
        We keep track of node from root to
        current level in "path" array.
        path = [rootNode, lvl2node, lvl3node..,, currNode]

        For currNode we consider all paths to 
        that node, from each prev level.
        path1 - rootNode to currNode
        path2 - lvl2 node to currNode .. so on.

        We pop the node after visiting its 
        children.
        '''
        if not node:
            return path

        path.append(node.value)

        if self.left:
            path = self.mainFunc(node.left, K, path)
        if self.right:
            path = self.mainFunc(node.right, K, path)

        # print(node.value, path)
        for i in range(len(path)):
            if sum(path[i:]) == K:
                print(path[i:])
        path.pop()

        return path


if __name__ == "__main__":

    root = BT(1)
    root.left = BT(3)
    root.left.left = BT(2)
    root.left.right = BT(1)
    root.left.right.left = BT(1)
    root.right = BT(-1)
    root.right.left = BT(4)
    root.right.left.left = BT(1)
    root.right.left.right = BT(2)
    root.right.right = BT(5)
    root.right.right.right = BT(2)

    root.printTree()
    print()

    root.mainFunc(root, 5)
