'''
1. Node class and BT class with only init func 
2. Create - level order insert
3. Read 
    - DFS: io/pre/post traversal - Time O(n) | Space O(w), w is max width of any level
    - BFS: level order traversal - Time O(n) | Space O(h), h is max height (recusrsion stack)
4. Update 
5. Delete refer BT_construction.py
'''


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

    def isThere(self, value):

        queue = [self.root]
        while queue:
            currentNode = queue.pop(0)

            if currentNode.value == value:
                return True

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

        return False
