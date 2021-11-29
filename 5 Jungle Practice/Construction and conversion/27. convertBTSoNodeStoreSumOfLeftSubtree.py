

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

    def convertBTToLeftSumTree(self, node):
        '''
        Change a Binary Tree so that every node 
        stores sum of all nodes in left subtree
        '''
        if not node:
            return 0
        elif not node.left and not node.right:
            return node.value

        leftSum = self.convertBTToLeftSumTree(node.left)
        rightSum = self.convertBTToLeftSumTree(node.right)

        node.value += leftSum

        return node.value + rightSum


if __name__ == '__main__':
    t = BT()
    t.root = Node(1)
    t.root.left = Node(2)
    t.root.right = Node(3)
    t.root.left.left = Node(4)
    t.root.left.right = Node(5)
    t.root.right.right = Node(6)
    '''
in   8 4 9 2 10 5 1 6 3 7
pre  1 2 4 8 9 5 10 3 6 7
post 8 9 4 10 5 2 6 7 3 1
    '''

    t.BFSLevelOrderTraversal()
    print()
    t.convertBTToLeftSumTree(t.root)
    print()
    t.BFSLevelOrderTraversal()
