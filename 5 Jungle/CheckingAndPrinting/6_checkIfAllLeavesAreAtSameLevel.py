

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

#

    def checkIfAllLeavesAreAtSameLevel(self, commonLeavesLevel=0, level=0):

        if not self:
            return False

        if self.left:
            result, commonLeavesLevel = self.left.checkIfAllLeavesAreAtSameLevel(
                commonLeavesLevel, level+1)
            if result is False:
                return False, commonLeavesLevel

        if self.right:
            result, commonLeavesLevel = self.right.checkIfAllLeavesAreAtSameLevel(
                commonLeavesLevel, level+1)
            if result is False:
                return False, commonLeavesLevel

        if not self.left and not self.right:
            currentLeafLevel = level
            print(self.value, commonLeavesLevel, level)
            if not commonLeavesLevel:
                commonLeavesLevel = currentLeafLevel
            elif currentLeafLevel != commonLeavesLevel:
                return False, commonLeavesLevel

        return True, commonLeavesLevel

    def checkIfAllLeavesAreAtSameLevelIter(self):
        if not self:
            return

        queue = [self]
        level = 0
        leafFound = False
        while queue:
            sizeOfCurrentLevel = len(queue)
            level += 1

            for i in range(sizeOfCurrentLevel):
                node = queue.pop(0)
                print('level:', level, 'val:', node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if not node.left and not node.right:
                    if leafFound == False:
                        leafFound = True
                    else:
                        print(self.value)
                        return False

        return True


if __name__ == "__main__":

    root = BT()
    # nodes = [1, 2, 3, 4, 5]
    # nodes = [10, 8, 2, 3, 5, 2, 0, 1, 2, 2, 3, 1, 1, 0, 3]
    nodes = list(range(1, 15))
    for i in nodes:
        root.insert(i)

    print(root.checkIfAllLeavesAreAtSameLevel())

    print()


'''
1. complete iter for 9
'''
