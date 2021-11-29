
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        if self.top is None:
            print('Empty List')
        else:
            topVal = self.top.value
            delNode = self.top
            self.top = self.top.next
            del delNode
            return topVal

    def peek(self):
        if self.top is None:
            print('Empty List')
        else:
            return self.top.value

    def show(self):
        node = self.top
        while node:
            print(node.value, end=" ")
            node = node.next
        print()


if __name__ == '__main__':
    s = Stack()
    for i in range(1, 11):
        s.push(i)

    s.show()
    s.pop()
    s.show()
