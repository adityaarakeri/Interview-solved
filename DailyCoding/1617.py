"""
This problem was asked by Microsoft.

You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:

L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.
Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLL.

Given the string ..R...L.L, you should return ..RR.LLLL.
"""

def push_dominoes(dominoes):
    n = len(dominoes)
    forces = [0] * n
    left_force = 0

    # First pass: simulate forces from the left
    for i in range(n):
        if dominoes[i] == 'R':
            left_force = n
        elif dominoes[i] == 'L':
            left_force = 0
        else:
            left_force = max(left_force - 1, 0)
        forces[i] += left_force
    print("Simulate forces from LEFT:")
    print(forces)

    right_force = 0

    # Second pass: simulate forces from the right
    for i in range(n - 1, -1, -1):
        if dominoes[i] == 'L':
            right_force = n
        elif dominoes[i] == 'R':
            right_force = 0
        else:
            right_force = max(right_force - 1, 0)
        forces[i] -= right_force
    
    print("Simulate forces from RIGHT:")
    print(forces)


    result = ""
    for force in forces:
        if force == 0:
            result += '.'
        elif force > 0:
            result += 'R'
        else:
            result += 'L'

    return result

# Example usage:
dominoes1 = ".L.R....L"
result1 = push_dominoes(dominoes1)
print(result1)  # Output: "LL.RRRLLL"

dominoes2 = "..R...L.L"
result2 = push_dominoes(dominoes2)
print(result2)  # Output: "..RR.LLLL"
