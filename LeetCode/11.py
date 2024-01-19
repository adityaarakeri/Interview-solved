"""
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
"""
from typing import List

def maxArea(height: List[int]) -> int:
    if len(height) < 1:
        return 0
    l,r = 0, len(height) - 1
    max_area = 0

    while l < r:
        area = (r - l) * min(height[l], height[r])
        max_area = max(area, max_area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area

q1 = [1,8,6,2,5,4,8,3,7]
q2 = [1,1]
q3 = []
print(maxArea(height=q1))
print(maxArea(height=q2))
print(maxArea(height=q3))