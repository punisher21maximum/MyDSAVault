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

# recursive
    def inOrderRecur(self, node):
        if not node:
            return

        if node.left:
            self.inOrderRecur(node.left)

        print(node.value, end=' ')

        if node.right:
            self.inOrderRecur(node.right)

    def preOrderRecur(self, node):
        if not node:
            return

        print(node.value, end=' ')

        if node.left:
            self.preOrderRecur(node.left)

        if node.right:
            self.preOrderRecur(node.right)

    def postOrderRecur(self, node):
        if not node:
            return

        if node.left:
            self.postOrderRecur(node.left)

        if node.right:
            self.postOrderRecur(node.right)

        print(node.value, end=' ')

# iterative
    def inOrderIterative(self):

        stack = []
        node = self.root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(node.value, end=' ')
                node = node.right

    def preOrderIterative(self):

        stack = []
        node = self.root
        while stack or node:
            if node:
                print(node.value, end=' ')
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right

    def postOrderIterativeUsingTwoStacks(self):
        '''
        USING TWO STACKS
        pre:        Root Left Right 
        post:       Left Right Root

        pre changed:Root Right Left   --- reverse of post
        '''

        reversePostOrder = []

        stack = []
        node = self.root
        while stack or node:
            if node:
                reversePostOrder.append(node.value)
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                node = node.left

        print(reversePostOrder[::-1])

    def postOrderIterativeUsingOneStack(self):
        '''
        USING ONE STACK
        post: left right root 
        - while node, keep going left
        - pop node, print
        - if node has right and right not visited, visit right then print node 

        important: how to know if right of node visited or not 
        - in stack, push right of node and then node 
        - when you pop node, if right of popped node same as stack's top node - first time/right not visited
        - else - second time/right visited
        '''

        stack = []
        node = self.root
        while stack or node:
            if node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and stack and stack[-1] == node.right:
                    stack.pop()
                    stack.append(node)
                    node = node.right
                else:
                    print(node.value, end=' ')
                    node = None

    def postOrderIterativeUsingHashTable(self):
        '''
        No stack, No recursion

        using hashtable to keep track if we have visited the popped nodes' right before
        if not - push back the node and add to hashtable
        else - visit/print the popped node
        '''

        hashTable = {}

        stack = []
        node = self.root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and node not in hashTable:
                    hashTable[node] = True
                    stack.append(node)
                    node = node.right
                else:
                    print(node.value, end=' ')
                    node = None


if __name__ == '__main__':
    t = BT()
    vals = list(range(1, 11))
    for i in vals:
        t.insert(i)
    '''
in  8 4 9 2 10 5 1 6 3 7 
pre 1 2 4 8 9 5 10 3 6 7 
post8 9 4 10 5 2 6 7 3 1
    '''
    print('in', end=' ')
    t.inOrderRecur(t.root)
    print('\npre', end=' ')
    t.preOrderRecur(t.root)
    print('\npost', end=' ')
    t.postOrderRecur(t.root)
    print()
    t.postOrderIterativeUsingTwoStacks()
    print()
    t.postOrderIterativeUsingOneStack()
    print()
    t.postOrderIterativeUsingHashTable()
