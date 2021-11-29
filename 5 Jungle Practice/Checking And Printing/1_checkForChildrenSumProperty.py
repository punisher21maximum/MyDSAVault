

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BT:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)

        if not self.root:
            self.root = newNode
            return

        queue = [self.root]
        while queue:
            currentNode = queue.pop(0)

            if not currentNode.left:
                currentNode.left = newNode
                return
            else:
                queue.append(currentNode.left)

            if not currentNode.right:
                currentNode.right = newNode
                return
            else:
                queue.append(currentNode.right)

    def BFSLevelOrderTraversal(self):
        if not self.root:
            return

        queue = [self.root]
        while queue:
            currentNode = queue.pop(0)

            print(currentNode.value, end=' ')

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

        return False

    def checkForChildrenSumProperty(self, node):
        '''
        Children Sum Property:
        Node.value = sum(node.left.value + node.right.value)
        '''
        if not node:
            return

        left, right = 0
        if node.left:
            left = node.left.value
            if not self.checkForChildrenSumProperty(node.left):
                return False
        if node.right:
            right = node.right.value
            if not self.checkForChildrenSumProperty(node.right):
                return False

        if left != right:
            return False

        return True


if __name__ == '__main__':
    t = BT()
    vals = list(range(1, 16))
    for i in vals:
        t.insert(i)
    '''
in   8 4 9 2 10 5 1 6 3 7
pre  1 2 4 8 9 5 10 3 6 7
post 8 9 4 10 5 2 6 7 3 1
    '''

    t.BFSLevelOrderTraversal()
    print()
