

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

        lastNode = self.getLastNodeCSLL()

        if lastNode is None:
            self.head = newNode
            self.head.next = self.head
            return

        newNode.next = self.head
        lastNode.next = newNode

    def insertAtStartCSLL(self, data):
        newNode = Node(data)

        lastNode = self.getLastNodeCSLL()

        if lastNode is None:
            self.head = newNode
            self.head.next = self.head
            return

        newNode.next = self.head
        lastNode.next = newNode
        self.head = newNode

    def insertAtIndexCSLL(self, index, data):
        if index < 0:
            return

        newNode = Node(data)
        if index == 0:
            self.insertAtStartCSLL(data)
            return

        prevNode = self.getNodeByIndexCSLL(index - 1)
        if prevNode is None:
            return

        newNode.next = prevNode.next
        prevNode.next = newNode

    def insertAfterNodeCSLL(self, givenNodeData, data):
        newNode = Node(data)
        givenNode = self.getNodeByValueCSLL(givenNodeData)

        newNode.next = givenNode.next
        givenNode.next = newNode


if __name__ == '__main__':

    sll = CircularSLL()
    # for i in range(1, 11):
    sll.insertAtIndexCSLL(7, 1)

    sll.printCSLL()
