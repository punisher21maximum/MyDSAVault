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

    def isThere(self, value):

        queue = [self.root]
        while queue:
            currentNode = queue.pop(0)

            if currentNode.value == value:
                return True

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

        return False
