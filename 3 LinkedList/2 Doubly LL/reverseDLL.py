
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def printDLL(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()

    def insertAtEnd(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def getNodeByValue(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    def reverseDLL(self):
        node = self.head
        while node:
            prev = node.prev
            node.prev = node.next
            node.next = prev
            node = node.prev
        self.tail = self.head
        self.head = prev.prev


if __name__ == '__main__':
    dll = DLL()
    for i in range(1, 6):
        dll.insertAtEnd(i)

    dll.printDLL()
    dll.reverseDLL()
    dll.printDLL()
