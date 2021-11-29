

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

# insert

    def insertAtEnd(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            node = self.head

            while node.next:
                node = node.next

            node.next = newNode

# update

    def updateAtStart(self, newData):
        if not self.head:
            print('Empty List')
            return

        self.head.data = newData

    def updateAtEnd(self, newData):
        if not self.head:
            print('Empty List')
            return

        lastNode = self.getLastNode()
        lastNode.data = newData

    def updateAtIndex(self, index, newData):
        if index == 0:
            self.updateAtStart(newData)
        elif index < 0:
            print('Negative index')
            return

        node = self.getNodeAtIndex(index)
        if node:
            node.data = newData
        else:
            print('Update index out of range')

    def updateByValue(self, data):
        node = self.getNodeByValue()
        if node:
            node.data = data
        else:
            print('Value not found')


if __name__ == '__main__':

    sll = SLL()
    for i in range(1, 11):
        sll.insertAtEnd(i)

    sll.printSLL()

    sll.updateAtIndex(10, 99)

    sll.printSLL()
