

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
            for _ in range(len(queue)):
                currentNode = queue.pop(0)

                print(currentNode.value, end=' ')

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)
            print()

        return False

    def p(self, node):
        if not node:
            return

        print(node.value)

        if node.left:
            self.p(node.left)

        if node.right:
            self.p(node.right)

    def getLevelOfNode(self, node, givenNode, level=0):
        if not node:
            return

        levelOfNode = None

        if node.value == givenNode:
            return level

        if node.left:
            levelOfNode = self.getLevelOfNode(
                node.left, givenNode, level+1
            )
            if levelOfNode:
                return levelOfNode

        if node.right:
            levelOfNode = self.getLevelOfNode(
                node.right, givenNode, level+1
            )
            if levelOfNode:
                return levelOfNode

    def mainFunc(self, node1, node2):
        '''
        Cousin: same level
        '''

        levelOfNode1 = self.getLevelOfNode(self.root, node1)
        levelOfNode2 = self.getLevelOfNode(self.root, node2)

        print('cousin?', levelOfNode1 == levelOfNode2)


if __name__ == '__main__':
    t = BT()
    vals = list(range(1, 32))
    for i in vals:
        t.insert(i)
    '''
    in   8 4 9 2 10 5 1 6 3 7
    pre  1 2 4 8 9 5 10 3 6 7
    post 8 9 4 10 5 2 6 7 3 1
    '''

    t.BFSLevelOrderTraversal()
    print()
    t.mainFunc(4, 5)
    # t.p(t.root)
