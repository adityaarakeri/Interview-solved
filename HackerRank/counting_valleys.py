"""
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

"""


# Complete the coutingValleys function below

def countingValleys(n, s):
    valleys = 0
    level = 0

    for c in s:
        if c is 'D':
            level -= 1
        elif c is 'U':
            level += 1

            if level is 0:
                valleys += 1
    return valleys


if __name__ == '__main__':
    steps = 'UDDDUDUU'
    awns = countingValleys(len(steps), steps)
    print(awns)
