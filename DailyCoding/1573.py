"""
This problem was asked by Sumo Logic.

Given a array that's sorted but rotated at some unknown pivot, in which all elements are distinct, find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors. It is guaranteed that the first and last elements are lower than all others.
"""

# O of N soln
# def return_peak1(arr):
#     peak_array = []
#     for i in range(len(arr)-1):
#         if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
#             peak_array.append(arr[i])
#             # return arr[i]
#         # else:
#         #     return 0
#     return max(peak_array)

# a1 = [1,2,3,4,5]
# a2 = [1,2,3,5,3,6,2,1]
# print(return_peak1(a1))
# print(return_peak1(a2))

# O of Log(N) soln
def find_peak_element(nums):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        # Check if mid is a peak
        if nums[mid] > nums[mid + 1]:
            high = mid  # Search in the left half
        else:
            low = mid + 1  # Search in the right half

    return nums[low]

# Example usage:
rotated_array1 = [7, 9, 10, 2, 5, 6]
rotated_array2 = [-7, -9, -10, -2, -5, -6]

print("Peak element:", find_peak_element(rotated_array1))
print("Peak element:", find_peak_element(rotated_array2))





        
