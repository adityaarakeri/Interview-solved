from itertools import chain


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


class WordSearch(object):
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.columns = len(puzzle[0])

    def lr(self, length):
        if length > self.columns:
            yield Point(0, 0), Point(0, 0), ""
        for i in range(self.rows):
            for j in range(self.columns - length + 1):
                word = self.puzzle[i][j:j+length]
                yield Point(j, i), Point(j + length - 1, i), word

    def reverse(self, name, length):
        for start, end, word in getattr(self, name)(length):
            yield end, start, ''.join(reversed(word))

    def ud(self, length):
        if length > self.rows:
            yield Point(0, 0), Point(0, 0), ""
        for i in range(self.columns):
            for j in range(self.rows - length + 1):
                word = "".join(self.puzzle[j+k][i] for k in range(length))
                yield Point(i, j), Point(i, j + length - 1), word

    def lurd(self, length):
        if length > self.rows or length > self.columns:
            yield Point(0, 0), Point(0, 0), ""

        for i in range(self.rows - length + 1):
            for j in range(self.columns - length + 1):
                word = "".join(self.puzzle[j+k][i+k] for k in range(length))
                yield Point(i, j), Point(i + length - 1, j + length - 1), word

    def ldru(self, length):
        if length > self.rows or length > self.columns:
            yield Point(0, 0), Point(0, 0), ""

        for i in range(length - 1, self.rows):
            for j in range(self.columns - length + 1):
                word = "".join(self.puzzle[i - k][j + k]
                               for k in range(length))
                yield Point(j, i), Point(j + length - 1, i - length + 1), word

    def du(self, length):
        return self.reverse("ud", length)

    def rl(self, length):
        return self.reverse("lr", length)

    def rdlu(self, length):
        return self.reverse("lurd", length)

    def ruld(self, length):
        return self.reverse("ldru", length)

    def search(self, word):
        length = len(word)
        iters = ["lr", "rl", 'ud', 'du', 'lurd', 'rdlu', 'ldru', 'ruld']
        iters = chain(*[getattr(self, i)(length) for i in iters])
        for start, end, w in iters:
            # print start, end, w
            if w == word:
                return (start, end)
