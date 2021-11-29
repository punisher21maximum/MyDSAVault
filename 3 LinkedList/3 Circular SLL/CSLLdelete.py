

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

    def getLastNodeCSLL(self):
        if self.head is None:
            return None
        elif self.head.next == self.head:
            return self.head

        node = self.head.next
        while node.next != self.head:
            node = node.next
        return node

    def getNodeByIndexCSLL(self, index):
        if index == 0:
            return self.head
        if self.head is None:
            return

        node = self.head.next
        for i in range(index-1):
            if node.next != self.head:
                node = node.next
            else:
                print('Index out of range')
                return None

        return node

    def getNodeByValueCSLL(self, data):
        if not self.head:
            return None
        elif self.head.data == data:
            return self.head

        node = self.head
        while node != self.head:
            if node.data == data:
                return node

        return None

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

    def deleteAtStartCSLL(self):
        if not self.head:
            return
        elif self.head.next == self.head:
            self.head = None
            return

        lastNode = self.getLastNodeCSLL()
        delNode = self.head
        lastNode.next = self.head.next
        del delNode
        self.head = lastNode.next

    def deleteAtEndCSLL(self):
        if not self.head:
            return
        elif self.head.next == self.head:
            self.head = None
            return

        prevOfLast = self.head
        node = self.head.next
        while node.next != self.head:
            prevOfLast = node
            node = node.next
        delNode = node
        prevOfLast.next = node.next
        del delNode

    def deleteAtIndexCSLL(self, index):
        if not self.head or index < 0:
            return
        elif index == 0:
            self.deleteAtStartCSLL()
            return

        prevNode = self.head
        node = self.head.next
        for i in range(index-1):
            if node.next != self.head:
                prevNode = node
                node = node.next
            else:
                print('index out of range')
                return

        delNode = node
        prevNode.next = node.next
        del delNode

    def deleteByValueCSLL(self, data):
        if not self.head:
            return
        elif self.head.data == data:
            self.deleteAtStartCSLL()
            return

        prevNode = self.head
        node = self.head.next
        while node != self.head:
            if node.data == data:
                delNode = node
                prevNode.next = node.next
                del delNode
                return
            prevNode = node
            node = node.next


if __name__ == '__main__':

    sll = CircularSLL()
    for i in range(1, 11):
        sll.insertAtEndCSLL(i)

    sll.deleteByValueCSLL(11)
    sll.printCSLL()
