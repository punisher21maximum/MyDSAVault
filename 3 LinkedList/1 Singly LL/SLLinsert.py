

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

    def insertAtStart(self, data):
        newNode = Node(data)

        newNode.next = self.head
        self.head = newNode

    def insertAtIndex(self, index, data):
        if index == 0:
            self.insertAtStart(data)
            return
        elif index < 0:
            print('index < 0')
            return
        elif not self.head and index != 0:
            print('empty list')
            return

        newNode = Node(data)
        node = self.head

        for i in range(index - 1):
            if node and node.next:
                node = node.next
            else:
                print('index out of range')
                return

        newNode.next = node.next
        node.next = newNode

    def insertAfterNode(self, givenNode, data):
        newNode = Node(data)
        node = self.head

        while node and node != givenNode:
            node = node.next

        if node:
            newNode.next = node.next
            node.next = newNode


if __name__ == '__main__':

    sll = SLL()
    for i in range(1, 11):
        sll.insertAtEnd(i)

    sll.printSLL()
