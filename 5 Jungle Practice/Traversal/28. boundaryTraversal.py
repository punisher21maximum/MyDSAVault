
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


# solution 1

    def printLeftBorder(self, node):
        if not node:
            return

        if node.left:
            print(node.value, end=' ')
            self.printLeftBorder(node.left)
        elif node.right:
            print(node.value, end=' ')
            self.printLeftBorder(node.right)

    def printBottomBorder(self, node):
        if not node:
            return

        if not node.left and not node.right:
            print(node.value, end=" ")

        self.printBottomBorder(node.left)
        self.printBottomBorder(node.right)

    def printRightBorder(self, node):
        if not node:
            return

        if node.right:
            print(node.value, end=' ')
            self.printLeftBorder(node.right)
        elif node.left:
            print(node.value, end=' ')
            self.printLeftBorder(node.left)

    def boundaryTraversal(self):

        self.printLeftBorder(self.root)
        self.printBottomBorder(self.root)
        self.printRightBorder(self.root)


# solution 2


    def boundaryTraversalIterative(self):
        '''
        1. Traversal 1: Do LOT, keep nodes level wise, in dict 
        {'level1': [1], 'level2: [2, 3]...}
        2. Traversal 2: left border - print first ele of each level except last level
        3. Traversal 3: bottom border - print last level
        4. Traversal 4: right border - print last ele of each level except last level
        '''
        pass


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
    t.boundaryTraversal()
