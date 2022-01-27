

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
        level = 1
        while queue:
            levelSize = len(queue)
            print('level', level, end=': ')
            level += 1
            for _ in range(levelSize):
                node = queue.pop(0)
                print(node.value, end=' ')

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()

    def reverseAlternateLevelsOFPerfectBTHelper(self, node1, node2, level):
        if not node1:
            return

        if level % 2 == 1:
            print('lvl', level, node1.value, node2.value)
            node1.value, node2.value = node2.value, node1.value
            print('-lvl', level, node1.value, node2.value)

        self.reverseAlternateLevelsOFPerfectBTHelper(
            node1.left, node2.right, level + 1)
        self.reverseAlternateLevelsOFPerfectBTHelper(
            node1.right, node2.left, level + 1)

    def reverseAlternateLevelsOFPerfectBT(self):
        self.reverseAlternateLevelsOFPerfectBTHelper(
            self.root.left, self.root.right, 1)


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
    t.reverseAlternateLevelsOFPerfectBT()
    print()
    t.BFSLevelOrderTraversal()
