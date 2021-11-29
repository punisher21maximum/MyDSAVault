
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arbit = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def printDLL(self):
        node = self.head
        lenn = 0
        while node:
            print(node.data, end=' ')
            node = node.next
            lenn += 1
        print()

        node = self.head
        for i in range(lenn):
            print(node.arbit.data, end=' ')
            node = node.next
        print()

    def insertAtEnd(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def getNodeByValue(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    def assignArbitPointer(self, arbitArray):
        node = self.head
        for i in range(len(arbitArray)):
            data = arbitArray[i]
            node.arbit = self.getNodeByValue(data)
            node = node.next

    def copyLinkListWithNextAndArbitPtr(self, list1):
        # copy as SLL
        node1 = list1.head
        while node1:
            data = node1.data
            self.insertAtEnd(data)
            node1 = node1.next

        # modify next of list1 to point to corresponsing node in copyList
        node1, node2 = list1.head, self.head
        while node1:
            prevNode1 = node1
            prevNode2 = node2
            node1 = node1.next
            node2 = node2.next
            prevNode1.next = prevNode2
            prevNode2.arbit = prevNode1
            print(prevNode1.data, prevNode2.data)

        # assign arbit ptr in copyList
        self.printDLL()
        node2 = self.head
        while node2:
            print(node2.data)
            node2.arbit = node2.arbit.arbit.next
            node2 = node2.next


if __name__ == '__main__':
    dll = DLL()
    for i in range(1, 6):
        dll.insertAtEnd(i)

    arbitArray = [3, 1, 5, 3, 2]
    dll.assignArbitPointer(arbitArray)

    dll.printDLL()

    copyDll = DLL()
    copyDll.copyLinkListWithNextAndArbitPtr(dll)
    copyDll.printDLL()
