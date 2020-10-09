import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from Important.CalculatePi import *

PI = 3.141592653589793 # Close enough
threshold = 0.01

def test_calculate_pi():
	pi_result = calculate_pi(iterations=100000)
	error = pi_result - PI 

	assert abs(error)<threshold

test_calculate_pi()