

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enQfront(self, value):
        newNode = Node(value)
        if self.front is None:
            self.front = self.rear = newNode
        else:
            newNode.next = self.front
            self.front.prev = newNode
            self.front = newNode

    def enQrear(self, value):
        newNode = Node(value)
        if self.front is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            newNode.prev = self.rear
            self.rear = newNode

    def deQfront(self):
        if self.front is None:
            print('Empty List')
        elif self.front.next is None:
            delNode = self.front
            self.front = self.rear = None
            del delNode
        else:
            delNode = self.front
            self.front = self.front.next
            self.prev = None
            del delNode

    def deQrear(self):
        if self.front is None:
            print('Empty List')
        elif self.front.next is None:
            delNode = self.front
            self.front = self.rear = None
            del delNode
        else:
            delNode = self.rear
            self.rear = self.rear.prev
            self.rear.next = None
            del delNode

    def show(self):
        node = self.front
        while node:
            print(node.value, end=' ')
            node = node.next
        print()


if __name__ == '__main__':
    q = Queue()
    for i in range(1, 11):
        q.enQrear(i)

    q.show()
    q.deQrear()
    q.show()
