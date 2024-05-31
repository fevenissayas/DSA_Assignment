class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert(self, value, position):
        new_node = Node(value)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            if not self.tail:
                self.tail = new_node
            return
        current = self.head
        for _ in range(position - 2):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next
        if current is None:
            raise IndexError("Position out of bounds")
        new_node.next = current.next
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def deleteAtPosition(self, position):
        if not self.head:
            raise IndexError("Position out of bounds")
        if position == 1:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return
        current = self.head
        for _ in range(position - 2):
            if current.next is None:
                raise IndexError("Position out of bounds")
            current = current.next
        if current.next is None:
            raise IndexError("Position out of bounds")
        current.next = current.next.next
        if current.next is None:
            self.tail = current

    def deleteAfterNode(self, prev_node_value):
        current = self.head
        while current and current.value != prev_node_value:
            current = current.next
        if current is None or current.next is None:
            raise ValueError("The given node is not present in the list or has no next node")
        current.next = current.next.next
        if current.next is None:
            self.tail = current

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def iterate(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def push(self, value):
        self.linked_list.prepend(value)

    def pop(self):
        if self.linked_list.head is None:
            raise IndexError("Pop from an empty stack")
        pop_value = self.linked_list.head.value
        self.linked_list.head = self.linked_list.head.next
        if self.linked_list.head is None:
            self.linked_list.tail = None
        return pop_value

    def peek(self):
        if self.linked_list.head is None:
            raise IndexError("Peek from an empty stack")
        return self.linked_list.head.value

    def isEmpty(self):
        return self.linked_list.head is None

    def display(self):
        return self.linked_list.iterate()