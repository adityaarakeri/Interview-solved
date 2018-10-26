"""
input:
n = 5
Result:
['1', '2', 'Fizz', '4', 'Buzz']

"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n ==0 or n ==1:
            return [str(n)]
        result = []
        for i in range(1, n+1):
            if i%3== 0 and i%5==0:
                result.append("FizzBuzz")
            elif i%3 == 0:
                result.append('Fizz')
            elif i%5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result
    
s = Solution()
print(s.fizzBuzz(15))