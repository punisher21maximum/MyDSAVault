SIZE = 100


class Stack:
    def __init__(self):
        self.top = -1
        self.stack = []

    def push(self, value):
        if self.top == SIZE - 1:
            print('FULL')
        else:
            self.top += 1
            self.stack.append(value)

    def pop(self):
        print('==>', self.top)
        if self.top == -1:
            print('EMPTY')
        else:
            self.top -= 1
            return self.stack.pop()

    def peek(self):
        if self.top == -1:
            print('EMPTY')
        else:
            print(self.stack[self.top])

    def show(self):
        print(self.stack)


if __name__ == '__main__':
    stack = Stack()

    for i in range(1, 11):
        stack.push(i)
    print(stack.top)
    stack.show()
    stack.pop()
    stack.show()
