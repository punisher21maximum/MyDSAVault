

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


def checkIfTreeTraversalOfTwoTreesIsSame(root1, root2):
    stack1, stack2 = [root1], [root2]
    node1, node2 = root1, root2

    while stack1 or stack2:
        if not stack1 or not stack2:
            return False

        node1 = stack1.pop()
        while node1 and (node1.left or node1.right):
            if node1.right:
                stack1.append(node1.right)
            if node1.left:
                node1 = node1.left

        node2 = stack2.pop()
        while node2 and (node2.left or node2.right):
            if node2.right:
                stack2.append(node2.right)
            if node2.left:
                node2 = node2.right

        print(node1.value, node2.value)
        if ((node1 and node2 and node1.value != node2.value)
                or (node1 and not node2)
                or (not node1 and node2)):
            print('here', node1.value, node2.value)
            return False

    return True


if __name__ == "__main__":

    root = BT()
    # nodes = [10, 8, 2, 3, 5, 2]
    # nodes = [10, 8, 2, 3, 5, 2, 0, 1, 2, 2, 3, 1, 1, 0, 3]
    nodes = list(range(1, 16))
    for i in nodes:
        root.insert(i)

    root.printTree()
    print()

    print(checkIfTreeTraversalOfTwoTreesIsSame(root, root))
