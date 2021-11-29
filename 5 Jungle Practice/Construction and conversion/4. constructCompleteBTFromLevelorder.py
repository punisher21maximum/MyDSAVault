import math


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

# solution 1:
    def completeBTFromLevelorder(self, levelorder):
        '''
        Approach:
        level order for complete BT will have 2^L
        no. of nodes on each level, L is level in L >= 0
        A queue will have prev level
        '''
        levels = math.ceil(math.log(len(levelorder), 2))

        root = node = Node(levelorder[0])
        queue = [node]
        idx = 1

        for level in range(1, levels):

            numLevelNodes = (2 ** level)
            if idx + numLevelNodes >= len(levelorder):
                numLevelNodes = len(levelorder) - idx

            for j in range(numLevelNodes//2):
                node = queue.pop()

                if idx + 2*j < len(levelorder):
                    node.left = Node(levelorder[idx + 2*j])
                else:
                    return root

                if idx + 2*j + 1 < len(levelorder):
                    node.right = Node(levelorder[idx + 2*j + 1])
                else:
                    return root

                queue.append(node.left)
                queue.append(node.right)

            idx += numLevelNodes

        return root

# solution 2: Time O(n)
    def completeBTFromLevelorderTwo(self, levelorder, root, i, n):
        if i >= n:
            return

        root = Node(levelorder[i])

        root.left = self.completeBTFromLevelorderTwo(levelorder,
                                                     root.left, 2 * i+1, n)
        root.right = self.completeBTFromLevelorderTwo(levelorder,
                                                      root.right, 2 * i+2, n)

        return root

# solution 3: Time O(n)
    def completeBTFromLevelorderThree(self, levelorder, root, i, n):
        '''
        Approach:
        find last parent node 
            lastNodeIdx = len(levelorder) - 1
            lastParent = (lastNodeIdx - 1 ) // 2 
        iterate from firstParent (0 idx) to lastParent 
            keep finding children 
            add children to the tree
        '''


if __name__ == '__main__':
    t = BT()
    vals = list(range(1, 11))
    # for i in vals:
    #     t.insert(i)
    '''
in   8 4 9 2 10 5 1 6 3 7
pre  1 2 4 8 9 5 10 3 6 7
post 8 9 4 10 5 2 6 7 3 1
    '''

    levelorder = list(range(1, 14))
    t.root = t.completeBTFromLevelorder(levelorder)
    # t.root = t.completeBTFromLevelorderTwo(levelorder,
    #                                        root=None, i=0, n=len(levelorder))
    print()
    t.BFSLevelOrderTraversal()
