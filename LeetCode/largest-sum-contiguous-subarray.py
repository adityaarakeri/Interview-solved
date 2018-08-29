#  find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.

# example: [-1, -2, 4, 3, 1, -1, -5]
# ans: 2+4+3 = 9

def largest_sum_of_sub_array(arr):

    max_so_far = 0
    max_ending_here = 0

    for num in arr:

        max_ending_here = max_ending_here + num
        
        if (max_ending_here < 0):
            max_ending_here = 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far

print (largest_sum_of_sub_array([-1,-2,4,3,1,-1,-5])) # 8

print (largest_sum_of_sub_array([-1,-2,4,-1,3,-2,-4]))