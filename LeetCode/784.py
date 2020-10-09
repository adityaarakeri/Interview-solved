"""
784. Letter Case Permutation

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

Input: S = "abc"
Output: ["abc", "Abc", "aBc", "abC", "ABc", "AbC", "aBC", "ABC"]
"""


class Solution(object):
    def letterCasePerm(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        S = list(S)
        result = ['']
        while S:
            last = S.pop()
            if (last.isalpha()):
                result = [last.lower() + x for x in result] + \
                    [last.upper() + x for x in result]
                print(result)
            else:
                result = [last + x for x in result]
                print(result)

        return result


s = Solution()
print(s.letterCasePerm('1a2bc'))
