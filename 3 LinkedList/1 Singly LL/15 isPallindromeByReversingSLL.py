

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

    def isPallindromeByReversingSLL(self):
        '''
        1. find the middle | if two mid nodes, choose right one
        2. reverse 2nd half of SLL
        3. check pallindrome 
        4. reverse back the 2nd half of SLL
        '''
        # find mid
        midNode = self.head
        lastNode = self.head

        while lastNode and lastNode.next:
            midNode = midNode.next
            lastNode = lastNode.next.next

        # reverse
        prev = None
        curr = midNode
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        headOfSecondHalf = prev

        # check pallindrome
        leftNode = self.head
        rightNode = headOfSecondHalf
        while leftNode.next != midNode and leftNode.data == rightNode.data:
            leftNode = leftNode.next
            rightNode = rightNode.next

        if leftNode.next == midNode:
            print('Pallindrome')
        else:
            print('Not Pallindrome')

        # unreverse
        prev = None
        curr = headOfSecondHalf
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        headOfSecondHalf = prev
        lastNodeOfFirstHalf = leftNode
        lastNodeOfFirstHalf.next = headOfSecondHalf


if __name__ == '__main__':

    sll = SLL()
    for i in range(1, 6):
        sll.insertAtEnd(i)
    for i in range(5, 0, -1):
        sll.insertAtEnd(i)
    sll.printSLL()

    sll.isPallindromeByReversingSLL()
    sll.printSLL()
