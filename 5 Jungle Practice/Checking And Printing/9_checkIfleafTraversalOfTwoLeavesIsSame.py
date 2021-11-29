

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

    def mainFunc(self, root1, root2):
        '''
        sol1 space O(m+n): travserse tree1, store leaves 
        in array traverse tree2, match leaves of two trees

        sol2: iterative traversal, traverse one leaf at a 
        time of for both trees
        '''
        stack1 = [root1]
        stack2 = [root2]

        while stack1 or stack2:
            if not stack1 or not stack2:
                return False

            node1 = stack1.pop()
            while node1:
                if not node1.left and not node1.right:
                    break

                if node1.left:
                    stack1.append(node1.left)
                if node1.right:
                    stack1.append(node1.right)

                node1 = stack1.pop()

            node2 = stack2.pop()
            while node2:
                if not node2.left and not node2.right:
                    break

                if node2.left:
                    stack2.append(node2.left)
                if node2.right:
                    stack2.append(node2.right)

                node2 = stack2.pop()

            print(node1.value, node2.value)
            if node1.value != node2.value:
                return False

        return True


if __name__ == '__main__':
    tree1 = BT()
    root1 = tree1.root
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.right.left = Node(6)
    root1.right.right = Node(7)

    tree2 = BT()
    root2 = tree2.root
    root2 = Node(0)
    root2.left = Node(1)
    root2.right = Node(5)
    root2.left.right = Node(4)
    root2.right.left = Node(6)
    root2.right.right = Node(7)
    # vals = list(range(1, 16))
    # for i in vals:
    #     t.insert(i)
    '''
    in   8 4 9 2 10 5 1 6 3 7
    pre  1 2 4 8 9 5 10 3 6 7
    post 8 9 4 10 5 2 6 7 3 1
    '''

    # t.BFSLevelOrderTraversal()
    print()
    print(tree1.mainFunc(root1, root2))
