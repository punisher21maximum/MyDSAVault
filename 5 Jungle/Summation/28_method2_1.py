class DLL:

    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

    def printDLL(self):
        node = self
        while node.prev:
            node = node.prev
        while node:
            print(node.data, end=' ')
            node = node.next


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


def verticalSumInBT(root, dll=None, horizontalDist=0):
    if not root:
        return

    if not dll.data:
        dll.data = root.value
    else:
        dll.data += root.value

    # print(root.value, dll.data)

    if root.right:
        if not dll.next:
            dll.next = DLL()
            dll.next.prev = dll

        verticalSumInBT(root.right, dll.next)

    if root.left:
        if not dll.prev:
            dll.prev = DLL()
            dll.prev.next = dll

        verticalSumInBT(root.left, dll.prev)


# codeEnd


def printPath(path, idx):

    for i in range(idx, len(path)):
        print(path[i])


if __name__ == "__main__":

    root = BT()
    nodes = list(range(1, 8))
    # nodes = [1, -2, 3, 4, 5, -6, 2]
    for n in nodes:
        root.insert(n)

    dll = DLL()
    verticalSumInBT(root, dll)
    print()
    dll.printDLL()
