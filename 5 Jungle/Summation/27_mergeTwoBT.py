

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


# code


def mergeTwoBT(root1, root2):
    if not root1 and not root2:
        return None
    if not root1:
        return root2
    if not root2:
        return root1

    root1.value += root2.value

    root1.left = mergeTwoBT(root1.left, root2.left)

    root1.right = mergeTwoBT(root1.right, root2.right)

    return root1


def mergeTwoBTIter(root1, root2):
    if not root1 and not root2:
        return None
    if not root1:
        return root2
    if not root2:
        return root1

    stack1, stack2 = [root1], [root2]

    while stack1 or stack2:
        node1, node2 = stack1.pop(), stack2.pop()

        node1.value += node2.value

        if node1.left and node2.left:
            stack1.append(node1.left)
            stack2.append(node2.left)
        elif not node1.left and node2.left:
            node1.left = node2.left

        if node1.right and node2.right:
            stack1.append(node1.right)
            stack2.append(node2.right)
        elif not node1.right and node2.right:
            node1.right = node2.right

    return root1


# codeEnd


def printPath(path, idx):

    for i in range(idx, len(path)):
        print(path[i])


if __name__ == "__main__":

    # root = BT()
    # nodes = list(range(1, 8))
    # # nodes = [1, -2, 3, 4, 5, -6, 2]
    # for n in nodes:
    #     root.insert(n)

    # Let us construct the first Binary Tree
    #     1
    #    / \
    #  2     3
    # / \     \
    # 4 5     6
    root1 = BT(1)
    root1.left = BT(2)
    root1.right = BT(3)
    root1.left.left = BT(4)
    root1.left.right = BT(5)
    root1.right.right = BT(6)

    # Let us construct the second Binary Tree
    #    4
    #   / \
    # 1    7
    # /   / \
    # 3   2 6
    root2 = BT(4)
    root2.left = BT(1)
    root2.right = BT(7)
    root2.left.left = BT(3)
    root2.right.left = BT(2)
    root2.right.right = BT(6)

    #     5
    #    / \
    #   3   10
    #  / \  / \
    # 7   5 2  6
    # mergeTwoBT(root1, root2)

    mergeTwoBTIter(root1, root2)
    root1.printTree()
