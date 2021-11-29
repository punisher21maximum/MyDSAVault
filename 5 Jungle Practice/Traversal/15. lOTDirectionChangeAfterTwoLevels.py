

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

    def height(self, node):
        if not node:
            return 0

        return 1 + max(self.height(node.left), self.height(node.right))

    def levelOrderTraversalSpiralRecursiveHelper(self, node, level, flag):
        if not node:
            return

        if level == 1:
            print(node.value, end=" ")

        if flag == 'L2R':
            if node.left:
                self.levelOrderTraversalSpiralRecursiveHelper(
                    node.left, level - 1, flag)

            if node.right:
                self.levelOrderTraversalSpiralRecursiveHelper(
                    node.right, level - 1, flag)
        else:
            if node.right:
                self.levelOrderTraversalSpiralRecursiveHelper(
                    node.right, level - 1, flag)

            if node.left:
                self.levelOrderTraversalSpiralRecursiveHelper(
                    node.left, level - 1, flag)

    # Worst - skewed trees: O(n^2)
    def levelOrderTraversalSpiralRecursive(self):

        direction = 4
        for level in range(1, self.height(self.root) + 1):
            if direction in [3, 4]:
                self.levelOrderTraversalSpiralRecursiveHelper(
                    self.root, level, 'L2R')

            else:
                self.levelOrderTraversalSpiralRecursiveHelper(
                    self.root, level, 'R2L')
            direction -= 1
            if direction == 0:
                direction = 4
            print()

    def levelOrderTraversalSpiralIterative(self):
        '''
        Deque
        '''

        queue = [self.root]

        level = 1
        levelSize = None
        nextLevelSize = len(queue)

        while queue:

            levelSize = nextLevelSize
            nextLevelSize = 0
            print('level', level, levelSize, (level + 3) % 4, end=': ')

            for _ in range(levelSize):
                if (level + 3) % 4 <= 1:
                    node = queue.pop(0)
                else:
                    node = queue.pop()

                print(node.value, end=' ')

                if (level + 3) % 4 <= 1:
                    if node.left:
                        queue.append(node.left)
                        nextLevelSize += 1

                    if node.right:
                        queue.append(node.right)
                        nextLevelSize += 1
                else:
                    if node.right:
                        queue.insert(0, node.right)
                        nextLevelSize += 1

                    if node.left:
                        queue.insert(0, node.left)
                        nextLevelSize += 1

            level += 1
            print()


if __name__ == '__main__':
    t = BT()
    vals = list(range(1, 64))
    for i in vals:
        t.insert(i)
    '''
in   8 4 9 2 10 5 1 6 3 7
pre  1 2 4 8 9 5 10 3 6 7
post 8 9 4 10 5 2 6 7 3 1
    '''

    t.BFSLevelOrderTraversal()
    print()
    # t.levelOrderTraversalSpiralRecursive()
    print()
    t.levelOrderTraversalSpiralIterative()
