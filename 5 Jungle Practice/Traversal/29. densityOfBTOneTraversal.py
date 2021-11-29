'''
disp - lateral/inO/preO/postO trav
insert
search/update
del
'''


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
    '''
    density = size / height
    '''

    def getHeightAndSize(self, node, size=0, currHeight=1, height=1):
        if not node:
            return 0, 0

        size += 1
        height = max(currHeight, height)

        if node.left:
            size, height = self.getHeightAndSize(node.left, size,
                                                 currHeight + 1, height)

        if node.right:
            size, height = self.getHeightAndSize(node.right, size,
                                                 currHeight + 1, height)

        return size, height

    def denistyOfBT(self):

        size, height = self.getHeightAndSize(self.root)
        print(size, height, size/height)


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
    t.denistyOfBT()
