import unittest
import r1_1
import r1_2
import r1_3
import r1_4


class Test(unittest.TestCase):
	def test_r1_1(self):
		self.assertTrue(r1_1.is_multiple(1, 1))
		self.assertTrue(r1_1.is_multiple(4, 1))
		self.assertRaises(ZeroDivisionError, r1_1.is_multiple, 0, 0)
		self.assertFalse(r1_1.is_multiple(-1, 10))

	def test_r1_2(self):
		self.assertTrue(r1_2.is_even(0))
		self.assertTrue(r1_2.is_even(2))
		self.assertTrue(r1_2.is_even(-2000))
		self.assertTrue(r1_2.is_even(33333334))
		self.assertFalse(r1_2.is_even(1))
		self.assertFalse(r1_2.is_even(-1))
		self.assertFalse(r1_2.is_even(21))
		self.assertFalse(r1_2.is_even(-123))

	def test_r1_3(self):
		self.assertTrue(r1_3.minmax([0, 100.0]) == (0, 100.0))
		self.assertTrue(r1_3.minmax([0, 100.0, 2, 3, 4]) == (0, 100.0))
		self.assertTrue(r1_3.minmax([0, 100.0, 2, 3, 4, 500]) == (0, 500.0))
		self.assertTrue(r1_3.minmax([2, 1]) == (1, 2))
		self.assertTrue(r1_3.minmax([2, 2]) == (2, 2))
		self.assertTrue(r1_3.minmax([2, -22]) == (-22, 2))
		self.assertTrue(r1_3.minmax(['a', 'b']) == ('a', 'b'))
		self.assertTrue(r1_3.minmax(['a', 'B']) == ('B', 'a'))
		self.assertRaises(TypeError, r1_3.minmax, ['a', 2])
		self.assertRaises(TypeError, r1_3.minmax, [0, 'a'])
		self.assertRaises(TypeError, r1_3.minmax, 0)

	def test_r1_4(self):
		self.assertTrue(r1_4.sum_squares(0) == 0)
		self.assertTrue(r1_4.sum_squares(-1) == 0)
		self.assertTrue(r1_4.sum_squares(-2) == 1)
		self.assertTrue(r1_4.sum_squares(1) == 0)
		self.assertTrue(r1_4.sum_squares(2) == 1)
		self.assertTrue(r1_4.sum_squares(3) == 5)
		self.assertTrue(r1_4.sum_squares(4) == 14)
		self.assertTrue(r1_4.sum_squares(-4) == 14)
		self.assertRaises(TypeError, r1_4.sum_squares, "a")
		self.assertRaises(TypeError, r1_4.sum_squares, [2])

	def test_r1_5(self):
		pass
	
	def test_r1_6(self):
		#n >=0
		#



if __name__ == "__main__":
	unittest.main()
