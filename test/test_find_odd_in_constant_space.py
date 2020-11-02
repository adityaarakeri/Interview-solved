import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from Company.find_odd_in_constant_space import test_solution

def test_find_odd_in_constant_space():
    assert test_solution()

