"""
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

"""


# Complete the coutingValleys function below

def countingValleys(n, s):
    valleys = 0
    level = 0

    for c in s:
        if c == 'D':
            level -= 1
        elif c == 'U':
            level += 1

            if level == 0:
                valleys += 1
    return valleys



steps = 'UDDDUDUU'
steps1 = 'DDUUUUDD'
print(countingValleys(len(steps), steps))
print(countingValleys(len(steps1), steps1))

