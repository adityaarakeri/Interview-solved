import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from Company.string_fill import string_fill


def test_string_fill():
    assert string_fill("abc", 2) == "abc"
    assert string_fill("abc", 7) == "    abc"

