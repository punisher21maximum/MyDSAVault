#  checkIfTreeIsSymmetric


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
'''
To check if a tree with root1 is symmetrical,
check if tree is mirror of itself,
pass two roots = root1 and root2 (root2 = root1)
'''


def checkIfTwoTreesIdentical(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    print(root1.value, root2.value)
    result = True

    if root1.left and root2.left:
        result = checkIfTwoTreesIdentical(root1.left, root2.left)
        if not result:
            return False

    if root1.right and root2.right:
        result = checkIfTwoTreesIdentical(root1.right, root2.right)
        if not result:
            return False

    if root1.value == root2.value:
        return True

    return False


def checkIfTwoTreesIdentical2(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    return (root1.value == root2.value and checkIfTwoTreesIdentical2(root1.left, root2.left)
            and checkIfTwoTreesIdentical2(root1.right, root2.right))


def checkIfTreeIsSymmetricIter(root1):
    if not root1:
        return True

    root2 = root1

    queue1, queue2 = [root1], [root2]
    while queue1 and queue2:
        node1, node2 = queue1.pop(0), queue2.pop(-1)

        print(node1.value, node2.value)
        printQ(queue1)
        printQ(queue2)

        if node1.value != node2.value:
            return False

        if node1.left and node2.right:
            queue1.append(node1.left)
            queue2.insert(0, node2.right)
        elif node1.left or node2.right:
            return False

        if node1.right and node2.left:
            queue1.append(node1.right)  # array.insert(key, value)
            queue2.insert(0, node2.left)
        elif node1.right and node2.left:
            return False

    return True


def printQ(q):
    print('-> ', end='')
    for n in q:
        print(n.value, end=' ')
    print()


if __name__ == "__main__":

    root1 = BT(1)
    root1.left = BT(2)
    root1.right = BT(2)
    root1.left.left = BT(3)
    root1.left.right = BT(4)
    root1.right.left = BT(4)
    root1.right.right = BT(3)

    root1.printTree()
    print()

    print(checkIfTreeIsSymmetricIter(root1))
