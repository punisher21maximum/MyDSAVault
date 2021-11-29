

class DLL:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def add(self, data):

        if not self.data:
            self.data = data
            return

        curr = self
        while curr.next:
            curr = curr.next

        curr.next = DLL(data, curr)

    def displayDLL(self):

        curr = self
        dll = []
        while curr:
            dll.append(curr.data)
            curr = curr.next
        print(dll)


class BT:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# util funcs
    def insert(self, value):

        if not self.value:
            self.value = value
            return

        queue = [self]

        while queue:
            currentNode = queue.pop(0)

            if not currentNode.left:
                currentNode.left = BT(value)
                break
            else:
                queue.append(currentNode.left)

            if not currentNode.right:
                currentNode.right = BT(value)
                break
            else:
                queue.append(currentNode.right)

    def levelOrderTraversalIterative(self):

        queue = []
        queue.append(self)

        while queue:
            currentNode = queue.pop(0)
            print(currentNode.value, end=' ')

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)


def BTtoDLL1(root):

    queue = [root]
    head = DLL()

    while queue:
        currentNode = queue.pop(0)
        head.add(currentNode.value)

        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

    return head


def BTtoDLL2inorder(root):

    if not root:
        return

    currentNode = root
    if root.left:
        inorderPredecessor = BTtoDLL2inorder(currentNode.left)

        while inorderPredecessor.right:
            inorderPredecessor = inorderPredecessor.right

        inorderPredecessor.right = currentNode
        currentNode.left = inorderPredecessor

    if root.right:
        inorderSuccessor = BTtoDLL2inorder(currentNode.right)

        while inorderSuccessor.left:
            inorderSuccessor = inorderSuccessor.left

        currentNode.right = inorderSuccessor
        inorderSuccessor.left = currentNode

    return currentNode

# BTtoDLLset2


def BTtoDLLtraverseInorderFixLeftPtrs(root):

    if not root:
        return

    BTtoDLLtraverseInorderFixLeftPtrs(root.left)

    root.left = BTtoDLLtraverseInorderFixLeftPtrs.inorderPredecessor
    BTtoDLLtraverseInorderFixLeftPtrs.inorderPredecessor = root

    BTtoDLLtraverseInorderFixLeftPtrs(root.right)

    return root


def BTtoDLLtraverseInorderFixRightPtrs(tail):

    previousNode = tail.left

    while previousNode:
        previousNode.right = tail
        tail = previousNode
        previousNode = tail.left

    return tail


def printDLL(head, direction='right'):

    currentNode = head
    if direction == 'right':
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.right
    else:
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.left


    ############################## main ###################################
    #
root = BT()
for i in range(1, 11):
    root.insert(i)
# root.levelOrderTraversalIterative()

# set 2

tail = root
while tail.right:
    tail = tail.right

# static variable for a function
BTtoDLLtraverseInorderFixLeftPtrs.inorderPredecessor = None

BTtoDLLtraverseInorderFixLeftPtrs(root)
printDLL(tail, 'left')
print()
head = BTtoDLLtraverseInorderFixRightPtrs(tail)
printDLL(head, 'right')
