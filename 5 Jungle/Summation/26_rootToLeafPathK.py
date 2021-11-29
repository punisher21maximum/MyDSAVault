

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


def rootToLeafPathK(root, givenPathSum, pathSum=0):
    if not root:
        return pathSum

    pathSum += root.value

    pathSum = rootToLeafPathK(
        root.left, givenPathSum, pathSum)
    pathSum = rootToLeafPathK(
        root.right, givenPathSum, pathSum)

    if not root.left and not root.right and pathSum == givenPathSum:
        print(root.value, pathSum, True)

    pathSum -= root.value

    return pathSum


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
    root = BT(10)
    root.left = BT(8)
    root.right = BT(2)
    root.left.right = BT(5)
    root.left.left = BT(3)
    root.right.left = BT(2)

    print(rootToLeafPathK(root, givenPathSum=21))
