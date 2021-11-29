from collections import defaultdict


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


    def diagonalTraversalHelper(self, node, resultDict, diagonalLevel=1):
        if not node:
            return

        resultDict[diagonalLevel].append(node.value)

        self.diagonalTraversalHelper(node.left, resultDict, diagonalLevel + 1)
        self.diagonalTraversalHelper(node.right, resultDict, diagonalLevel)

    def diagonalTraversal(self):  # Time O(Nlog(N)) | Space O(N)

        resultDict = defaultdict(list)
        self.diagonalTraversalHelper(self.root, resultDict)

        for level in range(1, len(resultDict) + 1):
            print(level, resultDict[level])


# solution 2

    def diagonalTraversalIterative(self):  # Time O(Nlog(N)) | Space O(N)
        if not self.root:
            return

        result = []

        queue = [self.root]
        node = None
        while queue:
            if not node:
                node = queue.pop(0)

            result.append(node.value)

            if node.left:
                queue.append(node.left)

            node = node.right

        print(result)


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

    # t.inOrderNoStackNoRecursionMorriseTraversal()
    print()
    t.BFSLevelOrderTraversal()
    print()
    t.diagonalTraversal()
    print()
    t.BFSLevelOrderTraversal()
    print()
    # t.postOrderIterativeUsingHashTable()
