class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0 or self.head is None:
            return -1
        current_node = self.head
        position = 0
        while current_node:
            if position == index:
                return current_node.data
            current_node = current_node.next
            position += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            self.addAtHead(val)
            return
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        position = 0
        while current_node:
            if position == index - 1:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
            position += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        current_node = self.head
        position = 0
        while current_node:
            if position == index - 1 and current_node.next:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            position += 1
