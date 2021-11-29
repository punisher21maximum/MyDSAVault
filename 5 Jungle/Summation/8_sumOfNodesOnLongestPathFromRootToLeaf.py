from collections import defaultdict
from functools import reduce


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

    def mainFunc(self, level=0, maxPathLen=0, maxLenPathSum=0, hashTable=defaultdict()):
        '''
        Ques:
        Find sum of nodes on longest path from
        root to leaf.

        Thoery:
        To find the longest path from root to leaf,
        we keep a hashTable, which has currentPath,
        stores a node from each level.

        Len of hashTable is path length. 

        We can have multiple maxLenPath, we need to
        pick one with maxSum.

        So we keep track of currMaxPathLen, maxLenPathSum.
        if currPathLen > currMaxPathLen:
            maxLenPathSum = currPathSum 
        elif currPathLen == currMaxPathLen:
            maxLenPathSum = max(currPathSum, maxLenPathSum)


        Approach:

        '''
        if not self:
            return False

        hashTable[level] = self.value

        currPathLen = len(hashTable)

        currPathSum = reduce(lambda res, val: res + val, hashTable.values())
        if currPathLen > maxPathLen:
            maxPathLen = currPathLen
            maxLenPathSum = currPathSum
        elif currPathLen == maxPathLen:
            maxLenPathSum = max(currPathSum, maxLenPathSum)

        print(self.value, hashTable, level)

        if self.left:
            maxPathLen, maxLenPathSum = self.left.mainFunc(
                level+1, maxPathLen, maxLenPathSum, hashTable)

        if self.right:
            maxPathLen, maxLenPathSum = self.right.mainFunc(
                level+1, maxPathLen, maxLenPathSum, hashTable)

        del hashTable[level]
        print('>', self.value, hashTable, level)

        return maxPathLen, maxLenPathSum


if __name__ == "__main__":

    root = BT()
    for i in range(1, 14):
        root.insert(i)

    root.printTree()
    print()

    print(root.mainFunc())
