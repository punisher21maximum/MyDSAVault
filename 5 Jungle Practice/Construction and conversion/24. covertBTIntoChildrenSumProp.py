

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

    def inorder(self, node):
        if not node:
            return

        self.inorder(node.left)

        print(node.value, end=' ')

        self.inorder(node.right)

    def covertBTToHaveChildrenSumProperty(self, node):
        if not node:
            return
        if not node.left and not node.right:
            return

        self.covertBTToHaveChildrenSumProperty(node.left)
        self.covertBTToHaveChildrenSumProperty(node.right)

        left, right = 0, 0
        if node.left:
            left = node.left.value

        if node.right:
            right = node.right.value

        diff = (left + right) - node.value

        if diff > 0:
            node.value = left + right
        elif diff < 0:
            self.addDiff(node, diff * -1)

    def addDiff(self, node, diff):
        if not node:
            return

        if node.left:
            node.left.value += diff
            self.addDiff(node.left, diff)

        if node.right:
            node.right.value += diff
            self.addDiff(node.right, diff)


if __name__ == '__main__':
    t = BT()
    t.root = Node(50)
    t.root.left = Node(7)
    t.root.right = Node(2)
    t.root.left.left = Node(3)
    t.root.left.right = Node(5)
    t.root.right.left = Node(1)
    t.root.right.right = Node(30)
    '''
in   8 4 9 2 10 5 1 6 3 7
pre  1 2 4 8 9 5 10 3 6 7
post 8 9 4 10 5 2 6 7 3 1
    '''

    t.inorder(t.root)
    print()
    t.covertBTToHaveChildrenSumProperty(t.root)
    print()
    t.inorder(t.root)
    print()
    t.BFSLevelOrderTraversal()
