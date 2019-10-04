"""
Test cases for ArrayPlusArray.py found in the CodeWars folder.

Answer by @mauricerivers
"""

# function to be tested
def array_plus_array(arr1,arr2):
    # variable used to add the array membeers
    sum = 0

    # loop through arr1 and add each item to sum
    for item in arr1:
        sum += item

    # loop through arr2 and add each item to sum
    for item in arr2:
        sum += item

    return sum

# function to test array_plus_array
def test_array_plus_array():
    assert array_plus_array([1, 2, 3], [4, 5, 6]) == 21, "Should be 21"
    assert array_plus_array([-1, -2, -3], [-4, -5, -6]) == -21, "Should be -21"

if __name__ == "__main__":
    test_array_plus_array()
    print("Everything passed")
