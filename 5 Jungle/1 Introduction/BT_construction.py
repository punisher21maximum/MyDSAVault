'''
Introduction:
1. Node class and BT class

CRUD
create - insert nodes 
read - traverse
update 
delete
'''


class BT:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):

        queue = []
        queue.append(self)

        while len(queue):
            currentNode = queue.pop()

            if currentNode.left == None:
                currentNode.left = BT(value)
                break
            else:
                queue.append(currentNode.left)

            if currentNode.right == None:
                currentNode.right = BT(value)
                break
            else:
                queue.append(currentNode.right)

    def isPresent(self, value):

        queue = []
        queue.append(self)

        while len(queue):
            currentNode = queue.pop()

            if currentNode.value == value:
                return True

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

        return False

    def remove(self, value):
        '''
        find node to be deleted, keep pointer to that node
        find a leaf node, assign value of leaf node to to_be_deleted node
        delete leaf node       
        '''

        # s1 - find toBeDeletedNode
        queue = []
        queue.append(self)

        while queue:
            currentNode = queue.pop()

            if currentNode.value == value:
                toBeDeletedNode = currentNode
                break

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

        # s2 - find any leaf node and keep a pointer to its parent node
        queue = []
        queue.append(self)
        currentNode = self

        while queue:
            parentNode = currentNode
            currentNode = queue.pop()

            if currentNode.left == None and currentNode.right == None:
                leafNode = currentNode
                break

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

        # s3
        if toBeDeletedNode:
            toBeDeletedNode.value = leafNode.value

            if parentNode.left == leafNode:
                parentNode.left = None
            else:
                parentNode.right = None

    def display(self):

        if not self:
            return

        if self.left:
            self.left.display()

        print(self.value)

        if self.right:
            self.right.display()


tree1 = BT(23)

for i in range(5):
    tree1.insert(i)
tree1.display()

tree1.remove(2)
print('------')
tree1.display()
