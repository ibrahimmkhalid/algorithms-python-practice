class Node:
    def __init__(self):
        self.value = None
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __repr__(self):
        if self.top is None:
            return "Empty"
        n = self.top
        data = ""
        while n is not None:
            data = data + " << " + str(n.value)
            n = n.next
        return data

    def push(self, value):
        item = Node()
        item.value = value
        item.next = self.top
        self.top = item
        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        item = self.top
        self.top = self.top.next
        self.size -= 1
        item.next = None
        return item.value

    def peek(self):
        if self.top is not None:
            return self.top.value
        return None


class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def __repr__(self):
        if self.front is None:
            return "Empty"
        n = self.front
        data = ""
        while n is not None:
            data = data + " >> " + str(n.value)
            n = n.next
        return data

    def enqueue(self, value):
        item = Node()
        item.value = value
        if self.back is None:
            self.front = item
            self.back = item
        else:
            self.back.next = item
            self.back = item
        self.size += 1

    def deque(self):
        item = self.front
        if item is None:
            return None
        elif self.front == self.back:
            self.front = None
            self.back = None
        else:
            self.front = item.next
        self.size -= 1
        return item.value

    def peek(self):
        if self.front is not None:
            return self.front.value
        return None


stack = Stack()
stack.push(1)
print(stack)
stack.push(2)
print(stack)
stack.push(3)
print(stack)
stack.push(4)
print(stack)
stack.push(5)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack)

queue = Queue()
queue.enqueue(1)
print(queue)
queue.enqueue(2)
print(queue)
queue.enqueue(3)
print(queue)
queue.enqueue(4)
print(queue)
queue.enqueue(5)
print(queue)
print(queue.deque())
print(queue.deque())
print(queue.deque())
print(queue.deque())
print(queue.deque())
print(queue.peek())
print(queue)
