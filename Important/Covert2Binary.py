# this is also known as divideby2 algorithm
import unittest

def ConvertToBinary(num):

    stack     = []
    binary = ''

    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    else:
        while num > 0:
            reminder = num % 2
            #push to stack
            stack.append(reminder)
            num = num // 2

        while len(stack) > 0:
            binary = binary + str(stack.pop())

        return binary

#print ConvertToBinary(int(raw_input("Enter a number to be converted to Binary > ")))

class Testconversion(unittest.TestCase):

    def test_zero(self):
        self.assertEquals(bin(0)[2:] , ConvertToBinary(0))

    def test_one(self):
        self.assertEquals(bin(1)[2:] , ConvertToBinary(1))

    def test_smallInt(self):
        self.assertEquals(bin(24)[2:] , ConvertToBinary(24))

    def test_LargeInt(self):
        self.assertEquals(bin(1000456)[2:] , ConvertToBinary(1000456))

if __name__ == '__main__':
    unittest.main(verbosity=2)
