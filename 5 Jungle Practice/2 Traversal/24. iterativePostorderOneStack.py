

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

    def postOrderIterativeUsingOneStack(self):
        '''
        USING ONE STACK
        post: Left Right Root 
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

    t.BFSLevelOrderTraversal()
    print()
