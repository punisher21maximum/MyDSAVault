

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def printSLL(self):
        node = self.head

        while node:
            print(node.data, end=' ')
            node = node.next
        print()

    def insertAtEnd(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            node = self.head

            while node.next:
                node = node.next

            node.next = newNode

    def isPallindromeByRecursion(self, leftNode, rightNode):
        if not rightNode:
            return leftNode

        result = self.isPallindromeByRecursion(leftNode, rightNode.next)
        if result is False:
            return False
        else:
            leftNode = result

        print(leftNode.data, rightNode.data)
        if leftNode.data != rightNode.data:
            print('Not Pallindrome')
            return False

        return leftNode.next


if __name__ == '__main__':

    sll = SLL()
    for i in range(1, 6):
        sll.insertAtEnd(i)
    for i in range(5, 0, -1):
        sll.insertAtEnd(i)

    sll.isPallindromeByRecursion(sll.head, sll.head)
