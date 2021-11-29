class LinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BT:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = TreeNode(value)

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

# solution 1: Time O(n)
    def completeBTFromLinkedList(self, linkedList):
        '''
        Approach:
        Set root of Tree as head of LL
        Then if curr LL node has next, add to tree 

        Pseudo:
        set root and node as head of LL
        queue = [node]
        while queue:
            node is queue.pop(0)
            if LL has next then set as left child else return root
            LL = LL.next 
            if LL has next then set as right child else return root
            LL = LL.next
        '''
        node = root = TreeNode(linkedList.data)
        queue = [node]
        while queue:
            node = queue.pop(0)

            if linkedList.next:
                node.left = TreeNode(linkedList.next.data)
                queue.append(node.left)
            else:
                return root
            linkedList = linkedList.next
            if linkedList.next:
                node.right = TreeNode(linkedList.next.data)
                queue.append(node.right)
            else:
                return root
            linkedList = linkedList.next


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

    # CREATE LINKEDLIST
    valsForLinkedList = [36, 30, 25, 15, 12, 10]
    headOfLL = LinkedListNode(valsForLinkedList[0])
    node = prev = headOfLL

    for val in valsForLinkedList[1:]:
        node = LinkedListNode(val)
        prev.next = node
        prev = node

    node = headOfLL
    while node:
        print(node.data, end=' ')
        node = node.next

    print()
    t.root = t.completeBTFromLinkedList(headOfLL)
    t.BFSLevelOrderTraversal()
