

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

    def perfectBTSpecificLOT(self):
        if not self.root:
            return

        result = []
        result.append(self.root.value)

        if not self.root.left:
            print(result)
            return
        else:
            result.append(self.root.left.value)
            result.append(self.root.right.value)

        if not self.root.left.left:
            print(result)

        queue = [self.root.left, self.root.right]
        while queue:
            leftNode = queue.pop(0)
            rightNode = queue.pop(0)

            if leftNode.left:
                '''
                why only check if leftNode.left > perfectBT
                no need to check for other ones.
                '''
                result.append(leftNode.left.value)
                result.append(rightNode.right.value)
                result.append(leftNode.right.value)
                result.append(rightNode.left.value)

                queue.append(leftNode.left)
                queue.append(rightNode.right)
                queue.append(leftNode.right)
                queue.append(rightNode.left)

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

    t.BFSLevelOrderTraversal()
    print()
    t.perfectBTSpecificLOT()
