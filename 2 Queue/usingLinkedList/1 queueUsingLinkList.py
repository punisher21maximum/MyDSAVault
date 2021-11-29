

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
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def deQ(self):
        if self.front is None:
            print('Empty List')
        elif self.front.next is None:
            delNode = self.front
            self.front = self.rear = None
            del delNode
        else:
            delNode = self.front
            self.front = self.front.next
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
        q.enQ(i)

    q.show()
    q.enQ(22)
    q.show()
