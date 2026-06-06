# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         pass
#
#     def hasNext(self):
#         pass
#
#     def next(self):
#         pass

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_element = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self.next_element

    def next(self):
        current = self.next_element
        self.next_element = self.iterator.next() if self.iterator.hasNext() else None
        return current

    def hasNext(self):
        return self.next_element is not None