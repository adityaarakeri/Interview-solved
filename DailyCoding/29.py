"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.

"""

def encoding(s):

    prev = s[0]
    count = 1
    result = ''

    for char in s[1:]:
        if char == prev:
            count += 1
            continue
        
        result += str(count) + prev
        prev = char
        count = 1

    return result + str(count) + prev


print(encoding('AAAABBBCCDAA'))