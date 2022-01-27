

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
            print('level', level, end=': ')
            for _ in range(levelSize):
                node = queue.pop(0) if level % 2 == 1 else queue.pop(-1)
                print(node.value, end=' ')

                if node.left:
                    queue.append(
                        node.left) if level % 2 == 1 else queue.insert(0, node.left)
                    nextLevelSize += 1
                if node.right:
                    queue.append(node.right) if level % 2 == 1 else queue.insert(
                        0, node.right)
                    nextLevelSize += 1
            level += 1
            print()

    def levelOrderTraversalSpiralIterativeTwo(self):  # O(n)
        if not self.root:
            return

        queue = [self.root, None]

        while len(queue) > 1:
            currentNode = queue.pop(0)

            if not currentNode:
                print()
                queue.append(None)
                continue

            print(currentNode.value, end=' ')

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

        return False


if __name__ == '__main__':
    t = BT()
    vals = list(range(1, 11))
    for i in vals:
        t.insert(i)
    '''
in   8 4 9 2 10 5 1 6 3 7
pre  1 2 4 8 9 5 10 3 6 7
post 8 9 4 10 5 2 6 7 3 1
    '''

    t.BFSLevelOrderTraversal()
    print()
    t.levelOrderTraversalSpiralIterativeTwo()
