

class Node:
    def __init__(self, data=None):

        self.data = data
        self.left = None
        self.right = None


def treeInsert(root, value):

    if not root.data:
        root.data = value
        return

    queue = [root]
    while queue:
        node = queue.pop(0)

        if not node.left:
            node.left = Node(value)
            break
        else:
            queue.append(node.left)

        if not node.right:
            node.right = Node(value)
            break
        else:
            queue.append(node.right)


def buildTree(root):

    for value in range(1, 11):
        treeInsert(root, value)


def printTree(root):

    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=' ')

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


class DLL:
    def __init__(self):

        self.head = None

    def BTtoDLL(self, root):

        if not root:
            return

        self.BTtoDLL(root.right)

        if self.head:
            self.head.left = root
            root.right = self.head
        self.head = root

        self.BTtoDLL(root.left)

    def printDLL(self):

        node = self.head
        print()
        while node:
            print(node.data, end=' ')
            node = node.right


if __name__ == "__main__":
    root = Node()
    buildTree(root)
    printTree(root)
    dll = DLL()
    dll.BTtoDLL(root)
    dll.printDLL()
