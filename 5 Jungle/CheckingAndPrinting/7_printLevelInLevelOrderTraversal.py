

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

    def printLevelInLevelOrderTraversal(self):
        if not self:
            return

        queue = [self]
        level = 0
        while queue:
            sizeOfCurrentLevel = len(queue)
            level += 1

            for i in range(sizeOfCurrentLevel):
                node = queue.pop(0)
                print('level:', level, 'val:', node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


if __name__ == "__main__":

    root = BT()
    # nodes = [10, 8, 2, 3, 5, 2]
    # nodes = [10, 8, 2, 3, 5, 2, 0, 1, 2, 2, 3, 1, 1, 0, 3]
    nodes = list(range(1, 16))
    for i in nodes:
        root.insert(i)

    root.printTree()
    print()

    print(root.printLevelInLevelOrderTraversal())


'''
1. complete iter for 9
'''
