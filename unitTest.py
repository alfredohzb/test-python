import unittest
import random

from main import filterData

class unitTest(unittest.TestCase):

	def test_values(self):
		inputHeight = str(random.randint(60,90))
		filterValues = filterData()
		filterValues.inputHeight = inputHeight
		result = filterValues.getResults()
		self.assertNotEqual(result,'No matches found')

if __name__ == '__main__':
	unittest.main()