

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

    def getLoopNode(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # print('-->', slow.data, fast.data)
            if slow == fast:
                loopNode = slow
                return loopNode

        return None

    def getLengthOfLoop(self):
        lengthOfLoop = 1
        loopNode = self.getLoopNode()
        if not loopNode:
            print('No Loop')
            return

        node = loopNode.next
        while node != loopNode:
            node = node.next
            lengthOfLoop += 1

        print(lengthOfLoop)
        return lengthOfLoop


if __name__ == '__main__':

    sll = SLL()
    for i in range(1, 11):
        sll.insertAtEnd(i)

    node = sll.head
    while node.next:
        node = node.next
    node.next = node
    print(sll.head.next.next.next.data)

    print(sll.getLengthOfLoop())
