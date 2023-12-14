"""
This problem was asked by Uber.

Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

"""

class TwoDIterator:
    def __init__(self, arrays):
        self.arrays = arrays
        self.row = 0
        self.col = 0
        self.move_to_next_non_empty()
    
    def move_to_next_non_empty(self):
        while self.row < len(self.arrays) and self.col == len(self.arrays[self.row]):
            self.row += 1
            self.col = 0

    def next(self):
        if not self.has_next():
            raise StopIteration("No more elements")

        result = self.arrays[self.row][self.col]
        self.col += 1
        self.move_to_next_non_empty()
        return result

    def has_next(self):
        return self.row < len(self.arrays)

# class StopIteration(Exception):


i = [[1, 2], [3], [], [4, 5, 6]]
iterator = TwoDIterator(i)
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next()) # < raises exception

