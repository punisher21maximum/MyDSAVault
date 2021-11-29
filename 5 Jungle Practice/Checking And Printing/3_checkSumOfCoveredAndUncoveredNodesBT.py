

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
            for _ in range(len(queue)):
                currentNode = queue.pop(0)

                print(currentNode.value, end=' ')

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)
            print()

        return False

    def sumOfLeftUncoveredNodes(self, node):
        if not node:
            return 0

        if node.left:
            return node.value + self.sumOfLeftUncoveredNodes(
                node.left
            )
        elif node.right:
            return node.value + self.sumOfLeftUncoveredNodes(
                node.right
            )
        else:
            return node.value

    def sumOfRightUncoveredNodes(self, node, summ=0):
        if not node:
            return 0

        if node.right:
            summ += self.sumOfRightUncoveredNodes(
                node.right
            )
        elif node.left:
            summ += self.sumOfRightUncoveredNodes(
                node.left
            )
        return node.value + summ

    def sumOfAllNodes(self, node, totalSum=0):
        if not node:
            return

        if node.left:
            totalSum += self.sumOfAllNodes(node.left)

        if node.right:
            totalSum += self.sumOfAllNodes(node.right)

        return totalSum + node.value

    def mainFunc(self):
        '''
        Uncovered Nodes:
        Nodes visible when viewed from top
        root - 1
        top left - 2, 4, 8, 9 
        top right - 3, 7, 15
                        1
                     /      \
                    2        3
                /      \  /       \
               4        5     6       7    
                 \    /  \   /  \    /  \ 
                   9 10  11 12  13  14   15
        Covered Nodes:
        remaining nodes 
        '''
        if not self.root:
            return True

        sumOfUncoveredNodes = self.root.value

        sumOfUncoveredNodes += self.sumOfLeftUncoveredNodes(self.root.left)
        sumOfUncoveredNodes += self.sumOfRightUncoveredNodes(self.root.right)

        sumOfAllNodes = self.sumOfAllNodes(self.root)

        print('left', self.sumOfLeftUncoveredNodes(self.root.left))
        print('right', self.sumOfRightUncoveredNodes(self.root.right))
        print('all', self.sumOfAllNodes(self.root))

        return sumOfAllNodes == 2 * sumOfUncoveredNodes


if __name__ == '__main__':
    t = BT()
    vals = list(range(1, 32))
    for i in vals:
        t.insert(i)
    '''
    in   8 4 9 2 10 5 1 6 3 7
    pre  1 2 4 8 9 5 10 3 6 7
    post 8 9 4 10 5 2 6 7 3 1
    '''

    t.BFSLevelOrderTraversal()
    print()
    print(t.mainFunc())
