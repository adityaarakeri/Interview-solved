def set_v(tree, focus, value):
    if not focus:
        tree['value'] = value
    else:
        for f in focus:
            tree[f] = set_v(tree[f], focus[1:], value)
    return tree


def set_direction(tree, direction, focus, item):
    if not focus:
        tree[direction] = item
    else:
        for f in focus:
            tree[f] = set_direction(tree[f], direction, focus[1:], item)
    return tree


class Zipper(object):
    def __init__(self, tree, focus=[]):
        self.tree = tree
        self.focus = focus

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def to_tree(self):
        return self.tree

    def value(self):
        tree = self.tree
        for direction in self.focus:
            tree = tree[direction]
        return None if tree is None else tree['value']

    def left(self):
        zipper = Zipper(self.tree, self.focus + ["left"])
        return None if zipper.value() is None else zipper

    def right(self):
        zipper = Zipper(self.tree, self.focus + ['right'])
        return None if zipper.value() is None else zipper

    def up(self):
        zipper = Zipper(self.tree, self.focus[:-1])
        return None if zipper.value() is None else zipper

    def set_value(self, value):
        return Zipper(set_v(self.tree, self.focus, value), self.focus)

    def set_left(self, item):
        return Zipper(
            set_direction(self.tree, "left", self.focus, item),
            self.focus,
        )

    def set_right(self, item):
        return Zipper(
            set_direction(self.tree, "right", self.focus, item),
            self.focus,
        )
