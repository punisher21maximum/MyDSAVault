

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

    def getLevelOfANode(self, nodeValue, level=0):
        if not self:
            return

        # print(self.value, level)

        resultLevel = -1

        if nodeValue == self.value:
            resultLevel = level
            return resultLevel

        if self.left:
            resultLevel = self.left.getLevelOfANode(
                nodeValue, level+1)
            if resultLevel != -1:
                return resultLevel
        if self.right:
            resultLevel = self.right.getLevelOfANode(
                nodeValue, level+1)
            if resultLevel != -1:
                return resultLevel

        return resultLevel

    def printCousinsOfAGivenNode(self, nodeValue, nodeLevel, cousins, currentLevel=0):
        if not self:
            return

        print(self.value, currentLevel)
        if nodeLevel - 1 == currentLevel:
            if ((not self.left or (self.left and self.left.value != nodeValue))
                    and (not self.right or (self.right and self.right.value != nodeValue))):

                if self.left:
                    cousins.append(self.left.value)
                if self.right:
                    cousins.append(self.right.value)

        if self.left:
            self.left.printCousinsOfAGivenNode(
                nodeValue, nodeLevel, cousins, currentLevel+1)

        if self.right:
            self.right.printCousinsOfAGivenNode(
                nodeValue, nodeLevel, cousins, currentLevel+1)

    def printCousinsOfAGivenNodeSingleTraversal(self, nodeValue, cousins):
        if not self:
            return

        queue = [self]
        level = -1
        nodeFound = False

        while queue and not nodeFound:
            levelLength = len(queue)
            level += 1
            print('level', level, ' :', end=' ')

            for i in range(levelLength):
                node = queue.pop(0)
                print(node.value, end=' ')

                if node.value != nodeValue:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    nodeFound = True
            print()

        for n in queue:
            # print(n.value, end=' ')
            cousins.append(n.value)


if __name__ == "__main__":

    root = BT()
    nodes = list(range(1, 16))
    for n in nodes:
        root.insert(n)

    root.printTree()
    print()

    nodeValue = 5
    cousins = []
    # nodeLevel = root.getLevelOfANode(nodeValue)
    # print('nodeLevel', nodeLevel)
    # # nodeLevel starts at 0
    # if nodeLevel in [0, 1]:
    #     print('no cousins')
    # else:
    #     root.printCousinsOfAGivenNode(nodeValue, nodeLevel, cousins)

    root.printCousinsOfAGivenNodeSingleTraversal(nodeValue, cousins)
    print(cousins)
