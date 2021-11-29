

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

    def checkAllLeavesAtSameLevel(self, node, level=0, leafLevel=None):
        if not node:
            return level

        if node.left:
            leafLevel = self.checkAllLeavesAtSameLevel(
                node.left, level+1, leafLevel
            )
            if leafLevel is False:
                return False

        if node.right:
            leafLevel = self.checkAllLeavesAtSameLevel(
                node.right, level+1, leafLevel
            )
            if leafLevel is False:
                return False

        if not node.left and not node.right:
            if not leafLevel:
                leafLevel = level
            elif leafLevel != level:
                return False

        print(node.value, leafLevel)
        return leafLevel

    def mainFunc(self, node1, node2):
        '''
        Cousin: same level
        '''


if __name__ == '__main__':
    t = BT()
    vals = list(range(1, 14))
    for i in vals:
        t.insert(i)
    '''
    in   8 4 9 2 10 5 1 6 3 7
    pre  1 2 4 8 9 5 10 3 6 7
    post 8 9 4 10 5 2 6 7 3 1
    '''

    # t.BFSLevelOrderTraversal()
    print()
    print(t.checkAllLeavesAtSameLevel(t.root))
