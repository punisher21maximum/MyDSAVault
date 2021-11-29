

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

    def main(self, numOfLevels):
        '''
        Given that the leaf nodes in this perfect binary 
        tree are starting from 1 to n, where n is the number 
        of leaf nodes. 

        And the parent node is the sum of the two child nodes.

        Approach:
        nodes are sum of children > total sum of each level is same.
        leaf nodes sum > sum of first N natural numbers > n(n+1)/2
        '''
        numOfNodesInLastLevel = 2 ^ (numOfLevels - 1)
        sumOfLastLevel = (numOfNodesInLastLevel *
                          (numOfNodesInLastLevel + 1))/2
        totalSumOfTree = sumOfLastLevel * numOfLevels

        return totalSumOfTree


if __name__ == "__main__":

    root = BT()

    for i in range(1, 8):
        root.insert(i)

    root.printTree()

    print(root.main())
    # print(root.sumOfLeftLeaves())
