from unittest import TestCase
import unittest
from sudoku_generator import get_all_sudokus,get_random_sudoku

class TestSudokuGenerator(TestCase):

	def test_get_all_sudokus(self):
		for l in range(1,5):
			suds=get_all_sudokus(l)
			for sud in suds:
				self.check(sud)

	def test_get_random_sudoku(self):
		sud=get_random_sudoku(9)
		self.check(sud)
		print("Random:")
		self.print_sud(sud)

	def print_sud(self,sud):
		for row in sud:
			print(row)

	def check(self,sud):
		n=len(sud)
		numbers=[i for i in range(1,n+1)]

		#check rows
		for row in sud:
			self.assertEqual(sorted(row),numbers)

		#check columns
		for n_col in range(n):
			col=[sud[i][n_col] for i in range(n)]
			self.assertEqual(sorted(col),numbers)

if __name__ == '__main__':
    unittest.main()


