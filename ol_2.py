class OrderedList:
    class Node:
        def __init__(self,data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.front = None
        self._size = 0

    def add(self,element):
        new_node = self.Node(element)
        if self.front is None or self.front.data >= element:
            new_node.next = self.front
            self.front = new_node
        else:
            current = self.front
            while current.next and current.next.data < element:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self._size += 1

    def remove_at(self,index):
        if index < 0 or index >= self._size:
            raise IndexError("Error out of bounds")
        if index == 0:
            return self.remove_first()
        current = self.front
        for _ in range(index-1):
            current = current.next
        removed = current.next
        current.next = removed.next
        self._size -=1
        return removed.data

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list")
        removed = self.front
        self.front = self.front.next
        self._size -= 1
        return removed.data

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list")
        if self._size == 1:
            return self.remove_first()
        current = self.front
        while current.next.next:
            current = current.next
        removed = current.next
        current.next = None
        self._size -= 1
        return removed.data

    def first(self):
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list")
        return self.front.data

    def last(self):
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list")
        current = self.front
        while current.next:
            current = current.next
        return current.data

    def get_at(self,index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        current = self.front
        for _ in range(index):
            current = current.next
        return current.data

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size