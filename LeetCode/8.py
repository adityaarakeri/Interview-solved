"""
8. String to Integer (atoi)
Medium
Topics
Companies
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

"""

def atoi(s: str) -> int:
    s = s.strip(' ')
    if len(s) <= 0:
        return 0
    else:
        # define the limits
        upper_limit = 2**31
        # strip of leading or trailing spaces
        s = s.strip(' ')
        # unicode limit of numbers 0 - 9
        # ord('0') = 48  abd ord('9') = 57
        result = 0
        is_negative = False

        if s[0] == '-':
            is_negative = True
        elif s[0] == '+':
            is_negative = False
        elif not s[0].isnumeric():
            return 0
        else:
            # start our result contruction
            result = ord(s[0]) - ord('0')
        
        # loop throu all digits from 1 position
        for i in range(1,len(s)):
            if s[i].isnumeric():
                result = result*10 + (ord(s[i]) - ord('0'))
                # print(result)
                if not is_negative and result >= upper_limit-1:
                    return upper_limit - 1
                elif is_negative and result >= upper_limit:
                    return -upper_limit
            else:
                break
                
        if is_negative:
            return -result
        else:
            return result
            

q1 = "42"
q2 = "   -42"
q3 = "4193 with words"
q4 = "words with 4193"
q5 = " "
q6 = "-"
print(atoi(q1))
print(atoi(q2))
print(atoi(q3))
print(atoi(q4))
print(atoi(q5))
print(atoi(q6))
