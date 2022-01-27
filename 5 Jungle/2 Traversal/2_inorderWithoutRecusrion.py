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

    def printTree(self):

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

    def inorderWithoutRecusrion(self):

        stack = [self.root]
        node = self.root

        while stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(node.value, end=', ')
                node = node.right


t1 = BT()

nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for node in nodes:
    t1.insert(node)

t1.printTree()
print()
t1.inorderWithoutRecusrion()
