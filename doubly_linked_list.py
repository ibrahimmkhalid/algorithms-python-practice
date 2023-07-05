import math
class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        p = "None" if self.prev == None else "Node"
        n = "None" if self.next == None else "Node"
        return p + " <- " + str(self.value) + " -> " + n
        

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
        pass

    def getLength(self) -> int:
        return self.length

    def __repr__(self) -> str:
        n = self.head
        if n == None:
            return "None"
        current_string = "None <- "
        while(n.next != None):
            current_string = current_string + str(n.value) + " <-> "
            n = n.next
        current_string = current_string + str(n.value) + " -> "
        current_string = current_string + "None"
        return current_string

    def prepend(self, value):
        item = Node()
        item.value = value
        item.next = self.head
        if self.head != None:
            self.head.prev = item
        else:
            self.tail = item
        self.head = item
        self.length += 1

    def append(self, value):
        item = Node()
        item.value = value
        item.prev = self.tail
        if self.tail != None:
            self.tail.next = item
        else:
            self.head = item
        self.tail = item
        self.length += 1

    def __get_node(self, index) -> Node:
        if index < math.floor(self.length / 2):
            n = self.head
            for _ in range(index):
                n = n.next
            return n
        else:
            n = self.tail
            for _ in range(self.length - 1, index, -1):
                n = n.prev
            return n
    def get(self, index):
        if index > self.length or index < 0:
            return None
        return self.__get_node(index).value

    def insertAt(self, index, value):
        if index >= self.length or index < 0:
            return None
        n = self.__get_node(index)
        item = Node()
        item.value = value
        if n.prev == None:
            self.head.prev = item
            item.next = self.head
            self.head = item
        else:
            n.prev.next = item
            item.prev = n.prev
            n.prev = item
            item.next = n
        self.length += 1

    def deleteAt(self, index):
        if index >= self.length or index < 0:
            return None
        n = self.__get_node(index)
        if n.prev == None:
            self.head = self.head.next
            if self.head == None:
                self.length -= 1
                return n.value
            self.head.prev = None
        else:
            n.prev.next = n.next
            if n.next == None:
                self.tail = n.prev
            else:
                n.next.prev = n.prev
            n.prev = None
            n.next = None
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
