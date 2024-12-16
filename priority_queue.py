from ordered_list import OrderedList

class PriorityQueue:
    def __init__(self):
        self._list = OrderedList()

    def enqueue(self, element):
        self._list.add(element)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._list.remove_first()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self._list.first()

    def is_empty(self):
        return self._list.is_empty()

    def size(self):
        return self._list.size()