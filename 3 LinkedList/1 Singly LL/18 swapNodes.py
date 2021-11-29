

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

    def getPrevNodeFromValue(self, data):
        '''
        if data is of head: return head
        for other nodes: return prev node
        '''
        if self.head.data == data:
            return self.head, self.head

        prev = self.head
        curr = self.head.next
        while curr:
            if curr.data == data:
                return prev, curr
            prev = curr
            curr = curr.next

        return None, None

    def swapNodes(self, data1, data2):
        prevOne, currOne = self.getPrevNodeFromValue(data1)
        prevTwo, currTwo = self.getPrevNodeFromValue(data2)

        oneIsHead, twoIsHead = False, False

        if currOne != self.head:
            prevOne.next = currTwo
        else:
            oneIsHead = True
        if currTwo != self.head:
            prevTwo.next = currOne
        else:
            twoIsHead = True

        nextOfTwo = currTwo.next
        currTwo.next = currOne.next
        currOne.next = nextOfTwo

        if oneIsHead:
            self.head = currTwo
        if twoIsHead:
            self.head = currOne


if __name__ == '__main__':

    sll = SLL()
    for i in range(1, 11):
        sll.insertAtEnd(i)

    sll.printSLL()
    sll.swapNodes(1, 4)

    sll.printSLL()
