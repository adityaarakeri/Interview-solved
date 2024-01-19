"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

import string
def encoding(message) -> int:
    if '0' in message:
        return "not allowed"
    else:
        all_letters = string.ascii_lowercase
        encoding_map = {}
        for i,e in enumerate(all_letters):
            encoding_map[e] = i+1 # as index starts from 0

        for i in range(1, len(message)):
            print(message[i:], message[:i])


def num_decodings(s):
    if not s:
        return 0

    n = len(s)
    dp = [0] * (n + 1)

    # Base case: an empty string has one decoding (no characters).
    dp[0] = 1

    # Check the first character of the string.
    if s[0] == '0':
        return 0
    dp[1] = 1

    for i in range(2, n + 1):
        # Check if the current character can be decoded individually.
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]

        # Check if the current and previous characters can be decoded together.
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]

# Example usage:
encoded_message = "111"
result = num_decodings(encoded_message)
print("Number of ways to decode:", result)

q1 = '111'
q2 = '110'
q3 = '001'
q4 = '1111'

result2 = num_decodings(q2)
print("Number of ways to decode:", result2)
result3 = num_decodings(q3)
print("Number of ways to decode:", result3)
result4 = num_decodings(q4)
print("Number of ways to decode:", result4)