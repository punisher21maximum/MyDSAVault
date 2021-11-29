
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


def verticalSumInBT(root, horizontalDist=0, verticalSumTable={}):
    if not root:
        return

    if horizontalDist in verticalSumTable:
        verticalSumTable[horizontalDist] += root.value
    else:
        verticalSumTable[horizontalDist] = root.value

    verticalSumInBT(root.left, horizontalDist-1, verticalSumTable)

    verticalSumInBT(root.right, horizontalDist+1, verticalSumTable)


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

    verticalSumTable = {}
    verticalSumInBT(root, 0, verticalSumTable)
    print(verticalSumTable)
