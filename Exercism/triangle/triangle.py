def is_triangle(func):
    def wrapped(sides):
        if any(i <= 0 for i in sides):
            return False
        sum_ = sum(sides)
        if any(sides[i] > sum_ - sides[i] for i in range(3)):
            return False
        return func(sides)
    return wrapped


@is_triangle
def is_equilateral(sides):
    return len(set(sides)) == 1


@is_triangle
def is_isosceles(sides):
    return len(set(sides)) != 3


@is_triangle
def is_scalene(sides):
    return len(set(sides)) == 3
