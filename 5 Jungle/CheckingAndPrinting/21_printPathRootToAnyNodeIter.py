

class BT:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

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


#

    def func(self, d=0):
        if not self:
            return self

        if self.left:
            self.left.func(d+1)
        if self.right:
            self.right.func(d+1)

        print(self.value, d)

    def func2(self, d=0, maxD=0):
        if not self:
            return self

        if self.left:
            maxD = self.left.func2(d+1)
        if self.right:
            maxD = self.right.func2(d+1)

        maxD = max(d, maxD)
        print(self.value, d, maxD)

        return maxD

    def func3(self, d=0, maxD=0):
        if not self:
            return self

        if self.left:
            maxD = self.left.func3(d+1, maxD)
        if self.right:
            maxD = self.right.func3(d+1, maxD)

        maxD = max(d, maxD)
        print(self.value, d, maxD)

        return maxD


# code


    def printPathRootToLeafIter(self):
        if not self:
            return

        stack = []
        node = self
        order = []
        path = []
        while True:
            while node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                path.append(node.value)
                node = node.left

            node = stack.pop()

            if node.right and stack and node.right == stack[-1]:
                stack.pop()
                stack.append(node)
                node = node.right
            else:
                if node and (not node.left and not node.right):
                    print(node.value, path)
                if path:
                    path.pop()
                order.append(node.value)
                node = None

            if not stack:
                break

        return order

    def printPathRootToAnyNodeIter(self):
        if not self:
            return

        stack = []
        node = self
        order = []
        path = []
        while True:
            while node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                path.append(node.value)
                node = node.left

            node = stack.pop()

            if node.right and stack and node.right == stack[-1]:
                stack.pop()
                stack.append(node)
                node = node.right
            else:
                print(node.value, path)
                if path:
                    path.pop()

                order.append(node.value)
                node = None

            if not stack:
                break

        return order


def printStack(arr):
    k = []
    for a in arr:
        k.append(a.value)
    return k


if __name__ == "__main__":

    root = BT()
    nodes = list(range(1, 32))
    for n in nodes:
        root.insert(n)

    root.printTree()
    print()

    # print(root.printPathRootToAnyNodeIter())
    # print(root.printPathRootToLeafIter())
    root.printOddLevelOfBT()
