

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

    def reverseTreePath(self, givenNode):
        if not self.root:
            return

        queue = [self.root]
        level = 1
        path = {}
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                node = queue.pop(0)
                path[level] = node
                if node.value == givenNode:
                    print(path)
                    return self.printPath(path, level)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            level += 1

    def reverseTreePathGivenPath(self, path, level):

        print(path)
        for i in range(1, (level // 2) + 1):
            path[i].value, path[level - i +
                                1].value = path[level - i + 1].value, path[i].value

    def getNodePath(self, node, givenNode, path={}, level=1):
        if not node:
            return

        path[level] = node

        if node.left:
            if self.getNodePath(node.left, givenNode,
                                path, level + 1):
                return

        if node.value == givenNode:
            self.reverseTreePathGivenPath(path, level)
            return True

        if node.right:
            if self.getNodePath(node.right, givenNode,
                                path, level + 1):
                return


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
    t.getNodePath(t.root, 12)
    print()
    t.BFSLevelOrderTraversal()
