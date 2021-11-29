

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

    def getLastNode(self):
        node = self.head

        while node.next:
            node = node.next

        return node

    def getNodeAtIndex(self, index):
        node = self.head

        for i in range(index):
            if node and node.next:
                node = node.next
            else:
                return None

        return node

    def getNodeByValue(self, data):
        node = self.head

        while node or node.data != data:
            node = node.next

        return node

    def insertAtEnd(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            node = self.head

            while node.next:
                node = node.next

            node.next = newNode

# delete

    def deleteAtStart(self):
        if not self.head:
            print('Empty List')
            return

        delNode = self.head
        self.head = self.head.next
        del delNode

    def deleteAtEnd(self):
        if not self.head:
            print('Empty List')
            return
        elif self.head.next is None:
            del self.head.next
        else:
            secondLastNode = self.head
            while secondLastNode.next.next:
                secondLastNode = secondLastNode.next
            lastNode = secondLastNode.next
            secondLastNode.next = None
            del lastNode

    def deleteAtIndex(self, index):
        if index == 0:
            self.deleteAtStart()
            return
        elif not self.head and index > 0:
            print('Delete index out of range')
            return

        prevOfIndexNode = self.getNodeAtIndex(index - 1)
        if prevOfIndexNode is None or prevOfIndexNode.next is None:
            print('Delete index out of range')
        else:
            delNode = prevOfIndexNode.next
            prevOfIndexNode.next = prevOfIndexNode.next.next
            del delNode

    def deleteByValue(self, data):
        node = self.getNodeByValue(data)
        if node:
            node.data = data
        else:
            print('Value not found')


if __name__ == '__main__':

    sll = SLL()
    for i in range(1, 11):
        sll.insertAtEnd(i)

    sll.printSLL()
