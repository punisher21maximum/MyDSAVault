
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


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

            if currentNode.next:
                print(currentNode.value, currentNode.next.value, '-', end=' ')
            else:
                print(currentNode.value, 'lastNode', '-', end=' ')

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

        return False

    def populateIndorderSuccForAllNodes(self):
        '''
        Quesion:
        Node has value, left, right, right.
        Initially next point to None.
        Next should point to inorderSucc

        Solution:
        Perform any inorder traversal (iterative with stack or morris or recursion)
        keep track of prev, set prev->next = curr

        Thoery:
        InorderSucc:
            > leftMostInRightSubtree or 
            > firstRightParent (node should be in leftSubtree of ancesstor)
        '''

        prev = None

        stack = []
        node = self.root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()

                if prev:
                    prev.next = node
                prev = node

                print(node.value, end=' ')
                if not node.right and not stack:
                    node.next = Node(-1)
                node = node.right

    def populateIndorderSuccForAllNodesRecursion(self, node, prev=None):
        if not node:
            return

        if node.left:
            prev = self.populateIndorderSuccForAllNodesRecursion(
                node.left, prev)

        if prev:
            prev.next = node
        prev = node

        print(node.value, end=' ')

        if node.right:
            prev = self.populateIndorderSuccForAllNodesRecursion(
                node.right, prev)

        # print('p', prev.value, end=':')
        return prev


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
    t.populateIndorderSuccForAllNodesRecursion(t.root)
    print()
    t.BFSLevelOrderTraversal()
