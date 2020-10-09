"""Question: Calculte the constant pi given a function that randomly returns a number between 0 and 1."""

from random import random 
from math import sqrt

def get_random_number():
	"""The given function. Returns random floating point number in the range [0.0, 1.0)."""
	return random()


def calculate_pi(iterations=10000000):
	"""
	Imagine a x,y-coordiante system. A cirlce with radius 1 is centerd at [0, 0]. 
	Now we create random points. Every point will be in the square [(0,0), (1,0), (0,1), (1,1)]. 
	If the distance from a point to the origin is smaller than 1, the point must be inside the cricle.
	
	The Area of the Square is one.
	The Area of the circle is pi/4 (since it is only a quarter of a full circle.)

	The ratio between points in the circle and all points approaches pi/4 as the iterations increase.

	"""
	points_in_circle = check_n_random_points(iterations)

	ratio_points_in_to_total = points_in_circle/iterations

	pi_estimate = ratio_points_in_to_total * 4 

	return pi_estimate


def check_n_random_points(n):
	points_in = 0

	for _ in range(n):
		if isInCircle(get_next_point_distance()):
			points_in += 1

	return points_in


def get_next_point_distance():
	x = random()
	y = random()
	return get_distance(x, y)


def get_distance(x, y):
	total = x*x + y*y
	length = sqrt(total)
	return length


def isInCircle(length):
	if length < 1:
		return True
	return False 


#print(calculate_pi())

