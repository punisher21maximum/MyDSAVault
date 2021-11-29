

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

    def segregateEvenAndOdd(self):

        firstOddNode = self.head
        while firstOddNode and firstOddNode.data % 2 == 0:
            firstOddNode = firstOddNode.next

        if firstOddNode.next:
            firstOddNode = firstOddNode.next
        else:
            return

        node = firstOddNode.next
        while node:
            if node.data % 2 == 0:
                firstOddNode.data, node.data = node.data, firstOddNode.data
                while firstOddNode and firstOddNode.data % 2 == 0:
                    firstOddNode = firstOddNode.next
                if firstOddNode.next:
                    firstOddNode = firstOddNode.next
                else:
                    return
            node = firstOddNode.next


if __name__ == '__main__':

    sll = SLL()
    k = [2, 2, 2, 2, 2, 1, 2, 3, 4, 5, 6]
    for i in k:
        sll.insertAtEnd(i)

    sll.segregateEvenAndOdd()
    sll.printSLL()
