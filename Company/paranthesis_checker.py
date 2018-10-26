"""
Check for Parenthesis in a given string

Example:
1.
Input: "abc{}abc"
Output: True

2. 
Input: "{}"
Output: True

3. 
Input: "{{}asd"
Output: False

"""

def para_checker(S):

    Stack = []
    para = {'{':0, '}':0}

    for i in S:
        if i == '{' or i == '}':
            Stack.append(i)
            if i=='{':
                para['{'] += 1
            if i=='}':
                para['}'] += 1
        
    return sum(para.values()) % 2 == 0 and Stack[0] == "{"

# A = 'abc{}abc'
# print(para_checker(A))

import unittest

class TestPara(unittest.TestCase):

    def test_check_positive(self):
        self.assertTrue(para_checker('abc{}abc'))
        self.assertTrue(para_checker('{}'))
        self.assertTrue(para_checker('{{asdasd}}'))

    def test_check_negative(self):
        self.assertFalse(para_checker('abc{}}'))
        self.assertFalse(para_checker('}{'))
        self.assertFalse(para_checker('}}{{'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
        

