

class Queue:
    def __init__(self, size):
        self.front = None
        self.rear = None
        self.queue = [None] * size
        self.size = size

    def enQ(self, value):
        '''
        empty 
        full
        rest
        '''
        if self.front is None:
            self.front = self.rear = 0
            self.queue[self.front] = value
        elif (self.rear + 1) % self.size == self.front:
            print('Queue Full')
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def deQ(self):
        '''
        empty
        one ele
        rest
        '''
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
            self.front = (self.front + 1) % self.size
            return frontVal

    def show(self):
        print(self.queue)


if __name__ == '__main__':
    q = Queue(10)
    for i in range(1, 11):
        q.enQ(i)
    q.show()

    for i in range(1, 6):
        q.deQ()
    q.show()

    for i in range(21, 26):
        q.enQ(i)
    q.show()
