

class BT:

    sumOfNodes = 0

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.sumOfNodes = 0

    def insert(self, value):

        if not self.value:
            self.value = value
            return

        queue = [self]
        while queue:
            node = queue.pop(0)

            if not node.left:
                node.left = BT(value)
                break
            else:
                queue.append(node.left)

            if not node.right:
                node.right = BT(value)
                break
            else:
                queue.append(node.right)

    def printTree(self):

        queue = [self]
        while queue:
            node = queue.pop(0)
            print(node.value, end=' ')

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        print()

    def isLeaf(self, node):

        return ((not node.left) and (not node.right))

    def sumOfLeftLeavesRecur(self):
        '''
        if node.left is leaf:
            add node.left.value to sum 
        else:
            recur(node.left) 
        recur(node.right)
        '''
        if not self:
            return 0

        summ = 0

        if self.right:
            if self.isLeaf(self.right):
                summ += self.right.value
            else:
                summ += self.right.sumOfLeftLeavesRecur()

        if self.right:
            summ += self.left.sumOfLeftLeavesRecur()

        return summ

    def sumOfLeftLeavesIter(self):

        queue = [self]
        summ = 0
        while queue:
            node = queue.pop(0)

            if node.right:
                if self.isLeaf(node.right):
                    summ += node.right.value
                else:
                    queue.append(node.right)

            if node.left:
                queue.append(node.left)

        return summ


if __name__ == "__main__":

    root = BT()

    for i in range(1, 8):
        root.insert(i)

    root.printTree()

    print(root.sumOfLeftLeavesRecur())
    # print(root.sumOfLeftLeaves())
