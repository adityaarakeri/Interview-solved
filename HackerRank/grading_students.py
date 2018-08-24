"""
https://www.hackerrank.com/challenges/grading/problem

"""
#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    final = []
    for grade in grades:
        if grade < 38:
            final.append(grade)
        else:
            if (grade%5 == 0) and grade > 38:
                final.append(grade)
            else:
                comp = helper(grade)
                diff = comp - grade
                result = grade + diff
                if diff < 3:
                    final.append(result)
                if diff >= 3:
                    final.append(grade)
    
    return final
        

def helper(grade):
    devisor = grade / 5
    devisor = devisor + 1
    result = devisor * 5
    return result
    

if __name__ == '__main__':

    n = int(raw_input())

    grades = []

    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
