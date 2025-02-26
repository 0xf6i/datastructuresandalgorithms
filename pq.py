from ol import OrderedList

class PriorityQueue:
    def __init__(self):
        self._list = OrderedList()

    def enqueue(self,element):
        self._list.add(element)

    def dequeue(self):
        if self._list.is_empty():
            raise IndexError("Cannot remove from an empty list")
        return self._list.remove_first()

    def peek(self):
        if self._list.is_empty():
            raise IndexError("Cannot remove from an empty list")
        return self._list.first()

    def is_empty(self):
        return self._list.is_empty()

    def size(self):
        return self._list.size()