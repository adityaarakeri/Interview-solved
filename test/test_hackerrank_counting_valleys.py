from HackerRank.counting_valleys import Solution

"""
    'D' represents one step down 
    'U' represents one step up 
    valley: is a sequence of consecutive steps below sea 
            level, starting with a step down from sea level and ending 
            with a step up to sea level

"""

def test1(sol):
    steps = 'UDDDUDUU'
    awns = sol.countingValleys(len(steps), steps)
    print('steps = '+steps)
    print("number of valleys = "+str(awns))


def test2(sol):
    steps = 'DDUUDDUDUUUD'
    awns = sol.countingValleys(len(steps), steps)

    print('steps = '+steps)
    print("number of valleys = "+str(awns))


sol = Solution()
test1(sol)
test2(sol)
