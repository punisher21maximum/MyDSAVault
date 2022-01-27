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

    def preOrderMorriseTraversal(self):

        node = self.root
        while node:
            if node.left:
                rightMostInLeftSubtree = node.left
                while rightMostInLeftSubtree.right != node and rightMostInLeftSubtree.right:
                    rightMostInLeftSubtree = rightMostInLeftSubtree.right

                if rightMostInLeftSubtree.right == node:
                    rightMostInLeftSubtree.right = None
                    node = node.right
                else:
                    print(node.value, end=' ')
                    rightMostInLeftSubtree.right = node
                    node = node.left
            else:
                print(node.value, end=' ')
                node = node.right


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

    # t.inOrderNoStackNoRecursionMorriseTraversal()
    print()
    t.BFSLevelOrderTraversal()
    print()
    t.preOrderMorriseTraversal()
    print()
    t.BFSLevelOrderTraversal()
    print()
    # t.postOrderIterativeUsingHashTable()
