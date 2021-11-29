

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enQ(self, value):
        newNode = Node(value)
        if self.front is None:
            newNode.next = newNode
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            newNode.next = self.front
            self.rear = newNode

    def deQ(self):
        if self.front is None:
            print('Empty List')
        elif self.front == self.rear:
            delNode = self.front
            self.front = self.rear = None
            del delNode
        else:
            delNode = self.front
            self.front = self.front.next
            del delNode
            self.rear.next = self.front

    def show(self):
        if not self.front:
            print('Empty List')
            return

        print(self.front.value, end=' ')
        node = self.front.next
        while node != self.front:
            print(node.value, end=' ')
            node = node.next
        print()


if __name__ == '__main__':
    q = Queue()
    for i in range(1, 11):
        q.enQ(i)

    q.show()
    q.enQ(22)
    q.show()
