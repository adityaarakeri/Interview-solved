import unittest

def Difference(lst1, lst2):

	if lst1 == [] or lst2 == []:
		return []
	else:
		diff1 = set(lst1).difference(set(lst2))
		diff2 = set(lst2).difference(set(lst1))

		union = diff1.union(diff2)

		return list(union)

# lst1 = [1,2,3,4,5,6]
# lst2 = [4,5,6,7,8,9]
# #ans [1,2,3,7,8,9]

# print Difference(lst1, lst2)

class TestDifference(unittest.TestCase):

	def test_equalLength(self):
		lst1 = [1,2,3,4,5,6]
		lst2 = [4,5,6,7,8,9]
		self.assertEqual([1,2,3,7,8,9], Difference(lst1, lst2))

	def test_empty(self):
		lst1=[]
		lst2=[1,2,3]
		self.assertEqual([],Difference(lst1,lst2))

	def test_single(self):
		lst1=[1]
		lst2=[2]
		self.assertEqual([1,2],Difference(lst1,lst2))

if __name__ == '__main__':
	unittest.main(verbosity=2)