import unittest

def BubbleSort(lst):

	for i in xrange(0 , len(lst)-1):
		for j in xrange(i+1, len(lst)):
			if lst[i] > lst[j]:
				lst[i], lst[j] = lst[j], lst[i]

	return lst

# print BubbleSort([1,5,4,3,6,7])
def BubbleSort1(lst):
    moreswaps=True

    while moreswaps:
        moreswaps=False
        for i in xrange(len(lst)-1):
            if lst[i] > lst[i+1]:
                moreswaps=True
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp

    return lst

class Test(unittest.TestCase):

	def test_sortedequal(self):
		self.assertEqual([1,2,3,4], BubbleSort([1,2,3,4]))

	def test_Unsorterequal(self):
		self.assertEqual([1,2,3,4], BubbleSort([4,3,2,1]))

	def test_sortedequalLarge(self):
		self.assertEqual([1,2,3,4,5,6,7,8,9,10], BubbleSort([1,2,3,4,5,6,7,8,9,10]))

	def test_UnsorterequalLarge(self):
		self.assertEqual([1,2,3,4,5,6,7,8,9,10], BubbleSort([10,9,8,7,6,5,4,3,2,1]))

	def test_empty(self):
		self.assertEqual([], BubbleSort([]))

	def test_single(self):
		self.assertEqual([1], BubbleSort([1]))


if __name__ == '__main__':
	unittest.main(verbosity=2)
