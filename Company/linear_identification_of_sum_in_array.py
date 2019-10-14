#!/usr/bin/python3

"""
The riddle (linear_identification_of_sum_in_array):
Given N integer numbers in an array and an integer number K, check if there are two 
numbers in the array that sums to K in linear average running time (O(N)).

"""

import numpy as np

N = 2000


def generate_random_input(n=N):
  """ n is the length of the generated array. returns the random array and a number K"""
  arr = np.random.randint(-5000, 5000, n)
  k = np.random.randint(-7500,7500)
  return arr, k
  
  
def solution(arr, k):
  """ build an hash map, insert k minus every element, iterate over original values and 
      check if they're contained in the array. """
  hash_map = {k - e: None for e in arr}
  for e in arr:
    if e in hash_map: // containment done in average O(1)
      return True
  return False
  

def false_test():
  arr = [-2,5,0,20]
  k = 7
  assert not solution(arr, k)
  

def positive_test():
  arr = [-2,5,0,20]
  k = 18
  assert solution(arr, k)
  
if __name__ == '__main__':
  false_test()
  positive_test()
  arr, k = generate_random_input()
  solution(arr, k)
