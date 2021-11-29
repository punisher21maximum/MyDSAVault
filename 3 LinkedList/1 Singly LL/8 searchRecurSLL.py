

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

    def searchRecurSLL(self, node, value):
        if not node:
            return False
        elif node.data == value:
            return True
        else:
            return self.searchRecurSLL(node.next, value)


if __name__ == '__main__':

    sll = SLL()
    for i in range(1, 11):
        sll.insertAtEnd(i)

    for i in range(-5, 15):
        print(i, sll.searchRecurSLL(sll.head, i))
