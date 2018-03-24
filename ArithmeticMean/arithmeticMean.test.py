import unittest
from arithmeticMean import arithmeticMean

class ArithmeticMeanTestCase(unittest.TestCase):
	def test_given_the_same_number_for_the_two_parameters_it_should_return_the_given_number(self):
		number = 2
		mean = arithmeticMean(number, number)

		self.assertEqual(mean, number)

unittest.main() 
