

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

    def reverseSLL(self):
        prev = None
        curr = self.head

        while curr:
            nextt = curr.next

            curr.next = prev

            prev = curr
            curr = nextt

        self.head = prev
        self.printSLL()


if __name__ == '__main__':

    sll = SLL()
    for i in range(1, 11):
        sll.insertAtEnd(i)

    sll.reverseSLL()
