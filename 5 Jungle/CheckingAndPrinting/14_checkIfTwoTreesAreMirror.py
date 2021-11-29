

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


def checkIfTwoTreesAreMirror(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    print(root1.value, root2.value)

    if root1.left and root2.right:
        if not checkIfTwoTreesAreMirror(root1.left, root2.right):
            return False

    if root1.right and root2.left:
        if not checkIfTwoTreesAreMirror(root1.right, root2.left):
            return False

    if root1.value == root2.value:
        return True

    return False


def checkIfTwoTreesAreMirror2(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    print(root1.value, root2.value)

    return (root1.value == root2.value and checkIfTwoTreesAreMirror(root1.left, root2.right) and
            checkIfTwoTreesAreMirror(root1.right, root2.left))


def checkIfTwoTreesAreMirrorIter(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    queue1, queue2 = [root1], [root2]
    while queue1 and queue2:
        node1, node2 = queue1.pop(0), queue2.pop(-1)

        print(node1.value, node2.value)

        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        if node1.value != node2.value:
            return False

        if node1.left:
            queue1.append(node1.left)
        if node1.right:
            queue1.append(node1.right)

        if node2.left:
            queue2.insert(0, node2.right)  # array.insert(key, value)
        if node2.right:
            queue2.insert(0, node2.left)

    return True


if __name__ == "__main__":

    root1 = BT(1)
    root2 = BT(1)

    root1.left = BT(2)
    root1.right = BT(3)
    root1.left.left = BT(4)
    root1.left.right = BT(5)

    root2.left = BT(3)
    root2.right = BT(2)
    root2.right.left = BT(5)
    root2.right.right = BT(4)

    root1.printTree()
    root2.printTree()
    print()

    print(checkIfTwoTreesAreMirrorIter(root1, root2))
