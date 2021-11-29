from collections import defaultdict


class BT:

    sumOfNodes = 0

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

    def mainFunc(self, rootVal, level=0, hashTable=defaultdict()):
        '''
        Ques:
        Checf if in root to leaf path, there is a pair,
        with sum equal to root's value.

        Approach:
        Keep track of path till current node.
        For root to current level, we will have
        one node for each level.
        Store node of each level in hash, which is path.
        For current node, check if in prev levels
        any node + curr node == root's value.
        '''
        if not self:
            return False

        hashTable[level] = self.value
        for lvl in range(1, level):
            if hashTable[lvl] + self.value == rootVal:
                print('---', lvl, hashTable, self.value, hashTable[lvl])
                return True

        print(self.value, hashTable, level)

        if self.left:
            if self.left.mainFunc(rootVal, level+1, hashTable):
                return True

        if self.right:
            if self.right.mainFunc(rootVal, level+1, hashTable):
                return True

        del hashTable[level]
        print('>', self.value, hashTable, level)

        return False


if __name__ == "__main__":

    root = BT()
    for i in range(1, 16):
        root.insert(i)
    # root.printTree()
    root = BT(8)
    root.left = BT(5)
    root.right = BT(4)
    root.left.left = BT(9)
    root.left.right = BT(7)
    root.left.right.left = BT(1)
    root.left.right.right = BT(12)
    root.left.right.right.right = BT(2)
    root.right.right = BT(11)
    root.right.right.left = BT(3)
    print()

    print(root.mainFunc(root.value))
