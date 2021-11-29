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

    def printTreeAsDLL(self):
        if not self.root:
            return

        node = self.root
        while node:
            print(node.value, end=' ')
            node = node.right


# solution 2: Time O(n) - Iterative


    def convertBTToDLLTwo(self):
        '''
        Question: convert tree into DLL
        Approach:
        Traverse in inorder fashion, add node to DLL
        Prerequisite: Iterative Morris Traversal
        '''
        node = self.root
        prev = None
        headOfDLL = None
        while node:
            if node.left:
                rightMostInLeftSubtree = node.left
                while rightMostInLeftSubtree.right != node and rightMostInLeftSubtree.right:
                    rightMostInLeftSubtree = rightMostInLeftSubtree.right

                if rightMostInLeftSubtree.right == node:
                    rightMostInLeftSubtree.right = None
                    # print(node.value, end=' ')
                    #
                    if prev:
                        prev.right = node
                        node.left = prev

                    prev = node
                    #
                    node = node.right
                else:
                    rightMostInLeftSubtree.right = node
                    node = node.left
            else:
                ##
                if not headOfDLL:  # set left most node as head
                    headOfDLL = node
                ##
                # print(node.value, end=' ')
                #
                if prev:
                    prev.right = node
                    node.left = prev
                prev = node
                #
                node = node.right

        return headOfDLL

    def covertBTToDLLThree(self):
        '''
        Question: Create new DLL, add tree nodes in inorder fashion

        # change tree to DLL
        1. iterative with stack:
        not tried, not possible maybe
        2. iterative w/o stack: (Morris Trav)
        Traverse, keep track of prev node
        set prev.right = node and node.left = prev
        head is before the first right node
        3. recursive:

        # new DLL from tree
        1. iterative with stack:
        traverse, add to DLL
        2. iterative w/o stack: (Morris Trav)
        traverse, add to DLL
        head is before the first right node
        3. recursive:
        traverse, add to DLL
        head is first in inorder

        '''


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
    # DLL

    t.root = t.convertBTToDLLTwo(t.root)
    t.printTreeAsDLL()
