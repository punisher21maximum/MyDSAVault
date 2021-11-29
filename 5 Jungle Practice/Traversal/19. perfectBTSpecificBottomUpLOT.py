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

    def getHeight(self, node):
        if not node:
            return 0

        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def perfectBTSpecificBottomUpLOTHelper(self, level):
        if not self.root:
            return

        result = []
        if level == 1:
            result.append(self.root.value)
            return result

        if not self.root.left:
            print(result)
            return

        queue = [self.root.left, self.root.right]
        currLevel = 2
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize//2):
                leftNode = queue.pop(0)
                rightNode = queue.pop(0)

                if level == currLevel:
                    result.append(leftNode.value)
                    result.append(rightNode.value)

                if leftNode.left:
                    queue.append(leftNode.left)
                    queue.append(rightNode.right)
                    queue.append(leftNode.right)
                    queue.append(rightNode.left)
            if currLevel == level:
                return result
            currLevel += 1

        return result

    def perfectBTSpecificBottomUpLOT(self):  # O(n^2)

        height = self.getHeight(self.root)
        for level in reversed(range(1, height + 1)):
            result = self.perfectBTSpecificBottomUpLOTHelper(level)
            print('level', level, result)

    def perfectBTSpecificBottomUpStackLOT(self):
        if not self.root:
            return

        resultStack = []
        resultStack.append(self.root.value)

        if not self.root.left:
            print(resultStack)
            return
        else:
            resultStack.append(self.root.right.value)
            resultStack.append(self.root.left.value)

        if not self.root.left.left:
            print(resultStack)

        queue = [self.root.left, self.root.right]
        while queue:
            leftNode = queue.pop(0)
            rightNode = queue.pop(0)

            if leftNode.left:
                resultStack.append(rightNode.left.value)
                resultStack.append(leftNode.right.value)
                resultStack.append(rightNode.right.value)
                resultStack.append(leftNode.left.value)

                queue.append(leftNode.right)
                queue.append(rightNode.left)
                queue.append(leftNode.left)
                queue.append(rightNode.right)

        print('reverse', resultStack[::-1])

    def perfectBTSpecificLOTBottumUpUsingHash(self):
        '''
        Best Answer:
        Traverse in same order but store in hash level wise
        {1: [1], 2: [2, 3], 3: [4, 7, 5, 6], 4: [8, 15, 9, 14, 10, 13, 11, 12]}
        '''
        if not self.root:
            return

        level = 1

        result = defaultdict(list)
        result[1] = [self.root.value]
        level += 1

        if not self.root.left:
            print(result)
            return
        else:
            result[level].append(self.root.left.value)
            result[level].append(self.root.right.value)
            level += 1

        if not self.root.left.left:
            print(result)

        queue = [self.root.left, self.root.right]
        while queue:
            for _ in range(len(queue)//2):
                leftNode = queue.pop(0)
                rightNode = queue.pop(0)

                if leftNode.left:
                    '''
                    why only check if leftNode.left > perfectBT
                    no need to check for other ones.
                    '''
                    result[level].append(leftNode.left.value)
                    result[level].append(rightNode.right.value)
                    result[level].append(leftNode.right.value)
                    result[level].append(rightNode.left.value)

                    queue.append(leftNode.left)
                    queue.append(rightNode.right)
                    queue.append(leftNode.right)
                    queue.append(rightNode.left)
            level += 1

        for i in reversed(range(1, len(result)+1)):
            print(result[i])

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
    t.perfectBTSpecificBottomUpStackLOT()
