class Node:
    def __init__(self):
        self.value = None
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0
        pass

    def getLength(self) -> int:
        return self.length

    def __repr__(self) -> str:
        n = self.head
        if n == None:
            return "None"
        current_string = ""
        while(n.next != None):
            current_string = current_string + str(n.value) + " -> "
            n = n.next
        current_string = current_string + str(n.value) + " -> "
        current_string = current_string + "None"
        return current_string

    def prepend(self, value):
        item = Node()
        item.value = value
        item.next = self.head
        self.head = item
        self.length += 1

    def append(self, value):
        item = Node()
        item.value = value
        if self.head == None:
            self.head = item
            self.length += 1
            return
        else:
            n = self.head
            for _ in range(self.length - 1):
                n = n.next
            n.next = item
            self.length += 1

    def get(self, index):
        if self.head == None or index > self.length - 1:
            return None
        elif self.head.next == None:
            return self.head.value
        else:
            n = self.head
            for _ in range(index - 1):
                n = n.next
            return n.value

    def insertAt(self, index, value):
        item = Node()
        item.value = value
        if index > self.length - 1:
            return -1
        if self.head == None:
            self.head = item
            self.length += 1
            return
        else:
            n = self.head
            p = None
            for _ in range(index):
                p = n
                n = n.next
            if p == None:
                item.next = n
                self.head = item
                self.length += 1
            else:
                p.next = item
                item.next = n
                self.length += 1

    def deleteAt(self, index):
        if index > self.length - 1:
            return -1
        if self.head == None:
            return None
        else:
            n = self.head
            p = None
            for _ in range(index):
                p = n
                n = n.next
            if p == None:
                self.head = None
                self.length = 0
            else:
                p.next = n.next
                self.length -= 1
            return n.value

list = LinkedList()


list.append(5)
list.append(7)
list.append(9)

print(list.get(2))
print(list.deleteAt(1))
print(list.length)

list.append(11)

print(list.deleteAt(1))
print(list.deleteAt(0))
print(list.deleteAt(0))
print(list.length)

list.prepend(5)
list.prepend(7)
list.prepend(9)

print(list.get(2))
print(list.get(0))
print(list.length)
list.deleteAt(0)
print(list.get(0))
