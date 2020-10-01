import unittest

from Exercism.two-fer.two_fer import two_fer

class Two_Fer(unittest.TestCase):
    def test_two_fer(name = ''):
        self.assertEqual(two_fer(name), "One for you, one for me")
    def test2_two_fer(name = 'name'):
        self.assertEqual(two_fer(name), "One for "+name+", one for me")


if __name__ == "__main__":
    unittest.main()
