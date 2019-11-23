Details of the challenge: https://www.hackerrank.com/challenges/jumping-on-the-clouds/

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    position = 0
    while position != len(c) - 1:
        if position != len(c) -2:
            if c[position + 2] is not 1:
                jumps += 1
                position  += 2
            elif c[position + 1] is not 1:
                jumps += 1 
                position += 1
        else:
            jumps += 1 
            position += 1 
    return jumps
