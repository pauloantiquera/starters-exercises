import unittest
from arithmeticMean import arithmeticMean

class ArithmeticMeanTestCase(unittest.TestCase):
	def test_given_the_same_number_for_the_two_parameters_it_should_return_the_given_number(self):
		number = 2
		mean = arithmeticMean(number, number)

		self.assertEqual(mean, number)
	
	def test_given_diferent_numbers_as_the_parameters_it_should_return_the_sum_of_the_numbers_divided_by_2(self):
		number1 = 5
		number2 = 43
		expectedMean = (number1 + number2) / 2

		mean = arithmeticMean(number1, number2)

		self.assertEqual(mean, expectedMean)

unittest.main() 
