"""
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

"""

"""
    'D' represents one step down 
    'U' represents one step up 
    valley: is a sequence of consecutive steps below sea 
            level, starting with a step down from sea level and ending 
            with a step up to sea level
            
"""

# Complete the coutingValleys function below
class Solution(object):
    def countingValleys(self,n, s):
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
    sol = Solution()
    steps = 'UDDDUDUU'
    awns = sol.countingValleys(len(steps), steps)
    print(awns)
