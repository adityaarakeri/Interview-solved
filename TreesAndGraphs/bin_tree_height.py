#!/usr/bin/python3

# The riddle:
#  find the height (longest path from the root node) of a binary tree (not necessarily balanced).


def depth(root):
    """ root is a tree node pointer that has access to left and right,
        returns the height of the tree + 1  """
    if root is None:
        return 0
    return 1 + max(depth(root.l), depth(root.r))

def solution(root):
    return depth(root) - 1


class T:
    def __init__(self, l=None, r=None):
        self.l = l
        self.r = r


def unit_test():
    assert solution(T(T(),T(T(), T()))) == 2
    assert solution(T(T(T(), T(T(None, T(T(),T())))), T(T()))) == 5

if __name__ == '__main__':
   unit_test()
