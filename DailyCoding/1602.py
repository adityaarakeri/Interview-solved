"""
This problem was asked by LinkedIn.

You are given a string consisting of the letters x and y, such as xyxxxyxyy. In addition, you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times you would need to apply this operation to ensure that all x's come before all y's. In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.

"""

def min_flips_to_order(s, type_flip):
    misplaced_y_count = 0
    flips_required = 0

    for char in s:
        if char == type_flip:
            flips_required += misplaced_y_count
        else:
            misplaced_y_count += 1

    return flips_required

# Example usage:
input_str = "xyxxxyxyy"
result = min_flips_to_order(input_str, "x")
print("Minimum flips required:", result)