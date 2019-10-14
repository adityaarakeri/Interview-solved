import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from Company.linear_identification_of_sum_in_array import false_test, positive_test

def test_linear_identification_of_sum_in_array():
    assert false_test()
    assert positive_test()
