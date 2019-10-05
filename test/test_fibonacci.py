from Company.fibonacci import fibonacci_recursive, fibonacci_iterative

def test_fibonacci_recursive():
    # check special cases
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(-1) == -1
    assert fibonacci_recursive(-10) == -10
    # check fibonacci sequence
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(5) == 5
    assert fibonacci_recursive(10) == 55
    assert fibonacci_recursive(20) == 6765

def test_fibonacci_iterative():
    # check special cases
    assert fibonacci_iterative(0) == 0
    assert fibonacci_iterative(1) == 1
    assert fibonacci_iterative(-1) == -1
    assert fibonacci_iterative(-10) == -10
    # check fibonacci sequence
    assert fibonacci_iterative(2) == 1
    assert fibonacci_iterative(5) == 5
    assert fibonacci_iterative(10) == 55
    assert fibonacci_iterative(20) == 6765

if __name__ == '__main__':
    test_fibonacci_iterative()
    test_fibonacci_recursive()
    print('passed')
