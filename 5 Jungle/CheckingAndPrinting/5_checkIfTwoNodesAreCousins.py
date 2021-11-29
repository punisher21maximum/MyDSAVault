

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

    def isNode1AndNode2AreSibling(self, node1, node2):

        if not self:
            return False

        isSibling = False

        if self.left:
            isSibling = isSibling or self.left.isNode1AndNode2AreSibling(
                node1, node2)
            if isSibling:
                return True

        if self.right:
            isSibling = isSibling or self.right.isNode1AndNode2AreSibling(
                node1, node2)
            if isSibling:
                return True

        if self.left and self.right:
            if ((self.left.value == node1 and self.right.value == node2) or
                    (self.left.value == node2 and self.right.value == node1)):
                return True

        return False

    def getLevelOfNode(self, node, level=0):
        if not self:
            return -1

        result = -1

        if self.value == node:
            return level

        if self.left:
            result = self.left.getLevelOfNode(node, level+1)
            if result != -1:
                return result

        if self.right:
            result = self.right.getLevelOfNode(node, level+1)
            if result != -1:
                return result

        return result

    def checkIfTwoNodesAreCousins(self, node1, node2):
        if not self:
            return False

        if (not self.isNode1AndNode2AreSibling(node1, node2)
                and self.getLevelOfNode(node1) == self.getLevelOfNode(node2)):
            return True

        return False


if __name__ == "__main__":

    root = BT()
    # nodes = [1, 2, 3, 4, 5]
    # nodes = [10, 8, 2, 3, 5, 2, 0, 1, 2, 2, 3, 1, 1, 0, 3]
    nodes = list(range(1, 16))
    for i in nodes:
        root.insert(i)

    print(root.checkIfTwoNodesAreCousins(10, 11))

    print()


'''
1. complete iter for 9
'''
