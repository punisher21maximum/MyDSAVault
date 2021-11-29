

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

    def countNodesInTree(self, node, count=0):
        if not node:
            return 0

        return (1 + self.countNodesInTree(node.left) +
                self.countNodesInTree(node.right))

    def checkIfRemovingNodeDivideTreeInTwoHalves(self, node, totalNodes):
        if not node:
            return False

        numOfNodesBelow = 0

        if node.left:
            result = self.checkIfRemovingNodeDivideTreeInTwoHalves(
                node.left, totalNodes
            )
            if result is True:
                return True
            numOfNodesBelow += result
        if node.right:
            result = self.checkIfRemovingNodeDivideTreeInTwoHalves(
                node.right, totalNodes
            )
            if result is True:
                return True
            numOfNodesBelow += result

        numOfNodesBelow += 1
        print(node.value, numOfNodesBelow, ':', totalNodes - numOfNodesBelow)
        if numOfNodesBelow == totalNodes - numOfNodesBelow:
            return True

        return numOfNodesBelow

    def mainFunc(self):
        '''
        Thoery:
        How to know the number of nodes in two subtrees formed
        when any node is deleted?
        Two trees: when a node is deleted, tree1 is below it with 
        this node as root and tree2 is of remaining nodes.
        Ans: 
        1. traversal 1: find total number of nodes in tree O(n)
        2. traversal 2: for each node find nodes below it.
        check nodes in tree1 == half of total nodes
        '''
        totalNodes = self.countNodesInTree(self.root)
        print(totalNodes)
        result = self.checkIfRemovingNodeDivideTreeInTwoHalves(
            self.root, totalNodes)
        print(result)


if __name__ == '__main__':
    t = BT()
    t.root = Node(5)
    t.root.left = Node(1)
    t.root.right = Node(6)
    t.root.left.left = Node(3)
    t.root.right.left = Node(7)
    t.root.right.right = Node(4)
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
    t.mainFunc()
