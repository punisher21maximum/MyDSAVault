

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

    def removeNodeByPrevNode(self, prev):
        delNode = prev.next
        prev.next = prev.next.next
        del delNode

    def removeDuplicatesFromUnsortedListHashing(self):
        '''
        Approach 1: Time O(NlogN) | Space O(N)
        Sort using mergeSort, then remove.

        Approach 2: Time O(N) | Space O(N) 
        Store visited in hashTable, if already
        visited, remove.
        '''
        prev = self.head
        curr = self.head.next
        hashTable = {self.head.data: True}

        while curr:
            if curr.data in hashTable:
                self.removeNodeByPrevNode(prev)
            else:
                hashTable[curr.data] = True
            curr = curr.next

        self.printSLL()
        print(hashTable, len(hashTable))


if __name__ == '__main__':

    sll = SLL()
    for i in range(1, 11):
        sll.insertAtEnd(i)
    for i in range(1, 11):
        sll.insertAtEnd(i)
    sll.printSLL()

    sll.removeDuplicatesFromUnsortedListHashing()
