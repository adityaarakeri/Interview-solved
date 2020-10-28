class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        output = []
        for i in candies:
            combined = i + extraCandies
            (output.append(True) if combined >= greatest else output.append(False)) 
        return (output)

'''
Runtime: 36 ms, faster than 75.41% of Python3 online submissions 
for Kids With the Greatest Number of Candies.
Memory Usage: 14.1 MB, 
less than 100.00% of Python3 online submissions for Kids With the Greatest Number of Candies.
'''