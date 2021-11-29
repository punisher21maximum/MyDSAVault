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

    def isLeaf(self, node):

        return (not node.left and not node.right)

    def mainFunc2(self, K, level=0, toBeDeleted=defaultdict(), hashTable=defaultdict()):
        '''
        Ques:
        For paths from root to leaf, remove nodes that 
        don't lie on any path with path sum >= k.

        Thoery:
        We keep a toBeDeleted, which has all nodes as keys
        and True as value if not to be deleted, False otherwise.

        Path - we keep track of path using hashtable,
        with node from each level above.

        When we reach any leaf node, a path from root to leaf
        is completed, we take sum of this path, if sum > X,
        for each node in path we set value as False in 
        toBeDeleted hash table.

        So at the end of whole process toBeDeleted has nodes
        with value True which are to be deleted.

        '''
        if not self:
            return

        hashTable[level] = self.value
        if self.isLeaf(self):
            currPathSum = sum(hashTable.values())
            if currPathSum > K:
                for node in hashTable.values():
                    toBeDeleted[node] = False

        print(self.value, hashTable, level)

        if self.left:
            return self.left.mainFunc2(
                K, level+1, toBeDeleted, hashTable)

        if self.right:
            return self.right.mainFunc2(
                K, level+1, toBeDeleted, hashTable)

        del hashTable[level]
        print('>', self.value, hashTable, level)

        return toBeDeleted

    def mainFunc(self, K):

        toBeDeleted = {}

        queue = [self]
        while queue:
            node = queue.pop(0)
            toBeDeleted[node] = False

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        toBeDeleted = self.mainFunc2(K)

        '''
        while toBeDeleted:
            for node in toBeDeleted:
                if isLeaf(node):
                    delete node 
                    
        '''


if __name__ == "__main__":

    root = BT()
    for i in range(1, 14):
        root.insert(i)

    root.printTree()
    print()

    print(root.mainFunc(K=10))
