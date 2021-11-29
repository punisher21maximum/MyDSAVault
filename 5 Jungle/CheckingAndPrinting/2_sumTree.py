

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

# sum of left subtree and right subtree == parent

    def isSumTree2(self):
        if not self:
            return 0

        leftAndRightSubtreeSum = 0
        if self.left:
            leftAndRightSubtreeSum += self.left.isSumTree2()

        if self.right:
            leftAndRightSubtreeSum += self.right.isSumTree2()

        if (self.left or self.right):
            if self.value == leftAndRightSubtreeSum:
                print(self.value, leftAndRightSubtreeSum, 'Yes')
            else:
                print(self.value, leftAndRightSubtreeSum, 'No')
        else:
            print(self.value, leftAndRightSubtreeSum, 'Yes')

        return self.value + leftAndRightSubtreeSum

# O(n*n)

    def isSumTree(self):
        if not self:
            return 0

        leftAndRightSubtreeSum = 0
        if self.left:
            leftSubtreeSum = self.left.isSumTree()
            if leftSubtreeSum is False:
                return False
            else:
                leftAndRightSubtreeSum += leftSubtreeSum

        if self.right:
            rightSubtreeSum = self.right.isSumTree()
            if rightSubtreeSum is False:
                return False
            else:
                leftAndRightSubtreeSum += rightSubtreeSum

        if (self.left or self.right) and self.value != leftAndRightSubtreeSum:
            return False

        return self.value + leftAndRightSubtreeSum

# O(n)

    def isSumTree(self):
        if not self:
            return 0

        leftAndRightSubtreeSum = 0
        if self.left:
            result, leftSubtreeSum = self.left.isSumTree()
            if result is False:
                return False, 0
            else:
                leftAndRightSubtreeSum += leftSubtreeSum

        if self.right:
            result, rightSubtreeSum = self.right.isSumTree()
            if result is False:
                return False, 0
            else:
                leftAndRightSubtreeSum += rightSubtreeSum

        if (self.left or self.right) and self.value != leftAndRightSubtreeSum:
            return False, 0

        if not self.left and not self.right:
            print(self.value, '1')
            return True, self.value
        else:
            print(self.value, '2')
            return True, self.value * 2


if __name__ == "__main__":

    root = BT()
    nodes = [26, 10, 3, 4, 6, 3, 1]
    # nodes = [10, 8, 2, 3, 5, 2, 0, 1, 2, 2, 3, 1, 1, 0, 3]
    # nodes = list(range(1, 16))
    for i in nodes:
        root.insert(i)

    root.printTree()
    print()

    print(root.isSumTree())
