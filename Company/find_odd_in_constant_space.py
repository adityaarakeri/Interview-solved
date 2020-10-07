#!/usr/bin/python3

"""
The riddle:
Given an array of N integer numbers, where all the numbers appear an even 
amount of time except for a single number that appears an odd amount of times.
Find the number that appears an odd amount of times in the array, using O(1) memory space 
and O(N) running time efficiency. 

Some examples:
[2,2,1] --> 1
[14,14,14,14,4,4,4] --> 4
[1,2,1,4,2,4,5,1,1] --> 5

"""
  
import numpy as np

N = 2000

def solution(arr):
  """ 
	Apply xor on all of the numbers, numbers that appear even amount of times cancel themselves
	using xor and the only number that appear an odd amount of times stays. 	

	@param List[int] arr : the array as described in the riddle documentation.
	@return int : the unique odd number.
  """
  if len(arr) == 0:
    raise ValueError('Wrong input format')
  stored = arr[0]   # O(1) space for integer storage
  for number in arr[1:]:  # linear traverse (O(N))
    stored ^= number
  return stored
 
def generate_random_test_array(n=N):
  """ returns a random array that fits the input requirements and the expected
      solution for that generated array. """
  assert n > 1
  half = np.random.randint(100, size=n//2)
  odd = half[0]
  full = np.hstack((half, half, [odd]))
  np.random.shuffle(full)
  return full, odd
  
 
def test_solution():
  if not solution([2,2,1]) == 1:
    return False
  if not solution([14,14,14,14,4,4,4]) == 4:
    return False
  if not solution([1,2,1,4,2,4,5,1,1]) == 5:
    return False
  for _ in range(10):
    arr, expected = generate_random_test_array()
    if not solution(arr) == expected:
      return False
  return True

