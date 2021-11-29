

class Queue:
    def __init__(self, size):
        self.front = None
        self.rear = None
        self.queue = [None] * size
        self.size = size

    def enQ(self, value):
        if self.rear == self.size - 1:
            print('Queue Full')
        elif self.front is None:
            self.front = self.rear = 0
            self.queue[self.front] = value
        else:
            self.rear += 1
            self.queue[self.rear] = value

    def deQ(self):
        if self.front is None:
            print('Empty Queue')
        elif self.front == self.rear:
            frontVal = self.queue[self.front]
            self.queue[self.front] = None
            self.front = self.rear = None
            return frontVal
        else:
            frontVal = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            return frontVal

    def show(self):
        print(self.queue[self.front:self.rear + 1])


if __name__ == '__main__':
    q = Queue(10)
    for i in range(1, 11):
        q.enQ(i)

    q.show()
    q.deQ()
    q.show()
