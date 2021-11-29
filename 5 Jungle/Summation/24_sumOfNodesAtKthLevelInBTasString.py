

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
'''
# How to identify level in treeAsAString
1. if '(' encountered --> level += 1
2. if ')' encountered --> level -= 1
'''


def sumOfNodesAtKthLevelInBTasString(treeAsAString, levelK=0):
    if not treeAsString:
        return 0

    level = -1
    summ = 0

    for i in range(len(treeAsAString)):
        if treeAsAString[i] == '(':
            level += 1
        elif treeAsAString[i] == ')':
            level -= 1
        elif level == levelK:
            summ += int(treeAsAString[i])

    return summ


# codeEnd
if __name__ == "__main__":

    s = '''(
        0
            (5
                (6
                    ()
                    ())
                (4
                    ()
                    (9
                        ()
                        ()      )))
            (7
                (1
                    ()
                    ())
                (3
                    ()
                    ()))
        )'''

    treeAsString = "(0(5(6()())(4()(9()())))(7(1()())(3()())))"
    print(sumOfNodesAtKthLevelInBTasString(treeAsString, levelK=2))
