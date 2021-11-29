

class BT:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):

        queue = []
        queue.append(self)

        while len(queue):
            currentNode = queue.pop(0)

            if currentNode.left == None:
                currentNode.left = BT(value)
                break
            else:
                queue.append(currentNode.left)

            if currentNode.right == None:
                currentNode.right = BT(value)
                break
            else:
                queue.append(currentNode.right)

    def display(self):

        if not self:
            return

        if self.left:
            self.left.display()

        print(self.value)

        if self.right:
            self.right.display()

# DFS
    def inorderTraversalRecursive(self):

        if not self:
            return

        if self.left:
            self.left.inorderTraversalRecursive()
        print(self.value, end=' ')
        if self.right:
            self.right.inorderTraversalRecursive()

    def preorderTraversalRecursive(self):

        if not self:
            return

        print(self.value, end=' ')
        if self.left:
            self.left.preorderTraversalRecursive()
        if self.right:
            self.right.preorderTraversalRecursive()

    def postorderTraversalRecursive(self):

        if not self:
            return

        if self.left:
            self.left.postorderTraversalRecursive()
        if self.right:
            self.right.postorderTraversalRecursive()
        print(self.value, end=' ')

    def inorderTraversalIterative(self):

        stack = []
        currentNode = self
        order = []

        while True:
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left

            if not stack:
                break

            currentNode = stack.pop()
            order.append(currentNode.value)

            currentNode = currentNode.right

        return order

    def preorderTraversalIterative(self):

        stack = []
        currentNode = self
        order = []

        while True:
            while currentNode:
                order.append(currentNode.value)
                stack.append(currentNode)
                currentNode = currentNode.left

            if not stack:
                break

            currentNode = stack.pop()

            currentNode = currentNode.right

        return order

    def postorderTraversalIterative2stacks(self):

        stack = []
        currentNode = self
        reverseOrder = []

        while True:
            while currentNode:
                reverseOrder.append(currentNode.value)
                stack.append(currentNode)
                currentNode = currentNode.right

            if not stack:
                break

            currentNode = stack.pop()

            currentNode = currentNode.left

        order = reverseOrder[::-1]
        return order

    def postorderTraversalIterative1stacks(self):

        stack = []
        currentNode = self
        order = []

        while True:
            while currentNode:
                if currentNode.right:
                    stack.append(currentNode.right)
                stack.append(currentNode)
                currentNode = currentNode.left

            currentNode = stack.pop()

            if currentNode.right and stack and currentNode.right == stack[-1]:
                stack.pop()
                stack.append(currentNode)
                currentNode = currentNode.right
            else:
                order.append(currentNode.value)
                currentNode = None

            if not stack:
                break

        return order

    def inorderTraversalMorris(self):

        currentNode = self
        while currentNode:
            if currentNode.left == None:
                print(currentNode.value, end=' ')
                currentNode = currentNode.right
            else:
                inorderPredecessor = currentNode.left
                while True:
                    if inorderPredecessor.right == None:
                        inorderPredecessor.right = currentNode
                        currentNode = currentNode.left
                        break
                    elif inorderPredecessor.right == currentNode:
                        inorderPredecessor.right = None
                        print(currentNode.value, end=' ')
                        currentNode = currentNode.right
                        break
                    else:
                        inorderPredecessor = inorderPredecessor.right

    def preorderTraversalMorris(self):

        currentNode = self
        while currentNode:
            if currentNode.left == None:
                print(currentNode.value, end=' ')
                currentNode = currentNode.right
            else:
                inorderPredecessor = currentNode.left
                while True:
                    if inorderPredecessor.right == None:
                        print(currentNode.value, end=' ')
                        inorderPredecessor.right = currentNode
                        currentNode = currentNode.left
                        break
                    elif inorderPredecessor.right == currentNode:
                        inorderPredecessor.right = None
                        currentNode = currentNode.right
                        break
                    else:
                        inorderPredecessor = inorderPredecessor.right

    def postorderTraversalMorris(self):

        currentNode = self
        visited = []
        while currentNode and currentNode not in visited:
            if currentNode.left and currentNode.left not in visited:
                currentNode = currentNode.left
            elif currentNode.right and currentNode.right not in visited:
                currentNode = currentNode.right
            else:
                print(currentNode)
                visited.append(currentNode)
                currentNode = self

# BFS
    def levelOrderTraversalIterative(self):

        queue = []
        queue.append(self)

        while queue:
            currentNode = queue.pop(0)
            print(currentNode.value, end=' ')

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

    def levelOrderTraversalRecursive(self):

        heightOfTree = self.height()
        for level in range(0, heightOfTree):
            self.levelOrderTraversalRecursiveHelper(level)

    def levelOrderTraversalRecursiveHelper(self, level):
        if not self:
            return
        if level == 0:
            print(self.value, end=' ')
        elif level > 0:
            self.left.levelOrderTraversalRecursiveHelper(level - 1)
            self.right.levelOrderTraversalRecursiveHelper(level - 1)

# height
    def height(self):
        if not self:
            return 0

        leftSubTreeHeight = self.left.height() if self.left else 0
        rightSubTreeHeight = self.right.height() if self.right else 0

        return 1 + max(leftSubTreeHeight, rightSubTreeHeight)


'''
main----------------------------------------------------------------
'''
tree1 = BT(1)
for i in range(2, 32):
    tree1.insert(i)


print(tree1.inorderTraversalIterative())

# print(tree1.preorderTraversalIterative())

# print(tree1.postorderTraversalIterative2stacks())

# print(tree1.levelOrderTraversalIterative())

# print(tree1.inorderTraversalMorris())
# print(tree1.preorderTraversalMorris())
