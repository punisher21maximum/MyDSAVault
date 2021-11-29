

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

    def updateAtStartCSLL(self, data):
        if not self.head:
            print('Empty List')
            return
        self.head.data = data

    def updateAtEndCSLL(self, data):
        if not self.head:
            print('Empty List')
            return
        lastNode = self.getLastNodeCSLL()
        lastNode.data = data

    def updateAtIndexCSLL(self, index, data):
        if not self.head:
            print('Empty List')
            return

        node = self.head
        for i in range(index):
            if node.next != self.head:
                node = node.next
            else:
                print('Out of range')
                return
        node.data = data

    def updateByValueCSLL(self, data, newData):
        if not self.head:
            print('Empty List')
            return
        elif self.head.data == data:
            self.head.data = newData
            return

        node = self.head.next
        while node != self.head:
            if node.data == data:
                node.data = newData
                return
            node = node.next

        print('Value not found')


if __name__ == '__main__':

    sll = CircularSLL()
    for i in range(1, 11):
        sll.insertAtEndCSLL(i)

    sll.updateByValueCSLL(11, 11)
    sll.printCSLL()
