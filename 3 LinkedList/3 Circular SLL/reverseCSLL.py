

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSLL:
    def __init__(self):
        self.head = None

    def printCSLL(self):
        if self.head:
            print(self.head.data, end=' ')
        else:
            print('Empty List')
            return

        node = self.head.next
        while node != self.head:
            print(node.data, end=' ')
            node = node.next
        print()

    def insertAtEndCSLL(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.head.next = self.head
        else:
            node = self.head.next

            while node.next != self.head:
                node = node.next

            newNode.next = self.head
            node.next = newNode

    def reverseCSLL(self):
        if self.head is None or self.head.next == self.head:
            return

        prev = self.head
        curr = self.head.next

        while curr != self.head:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt

        self.head.next = prev
        self.head = prev


if __name__ == '__main__':

    sll = CircularSLL()
    for i in range(1, 4):
        sll.insertAtEndCSLL(i)

    sll.reverseCSLL()
    sll.printCSLL()
