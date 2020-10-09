
import unittest
from Implementing_Dequeue import Dequeue


def Palindrome(string):

    if string == '':
        return False

    if len(string) == 1:
        return True

    return string.lower() == string[::-1].lower()


def Palindrome1(string):

    charDequeue = Dequeue()

    for ch in string:
        charDequeue.addFront(ch)

    stillEqual = True

    while charDequeue.size() > 1 and stillEqual:
        first = charDequeue.removeFront()
        last = charDequeue.removeRear()

        if first != last:
            stillEqual = False

    return stillEqual

# print Palindrome1(input("Is this a Palindrome? : "))


class test_Palindrome(unittest.TestCase):

    def testPalindrome(self):
        self.assertEqual(Palindrome("radar"), True)

    def testPalindrome1(self):
        self.assertEqual(Palindrome1("radar"), True)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("Palindrome('12321')",
                        setup="from __main__ import Palindrome"))
    print(timeit.timeit("Palindrome1('radar')",
                        setup="from __main__ import Palindrome1"))
    unittest.main(verbosity=2)
