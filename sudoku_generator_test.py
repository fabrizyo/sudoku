from unittest import TestCase
import unittest
from sudoku_generator import get_random_sudoku

class TestSudokuGenerator(TestCase):

	def test_get_random_sudoku(self):
		sud=get_random_sudoku()
		self.check(sud)
		print("Random:")
		self.print_sud(sud)
		print()
		remove=10
		sud=get_random_sudoku(remove)
		count=0
		for row in range(9):
			for col in range(9):
				count+=1 if sud[row][col] is None else 0
		self.assertEqual(remove,count)
		print("Random remove")
		self.print_sud(sud)

	def print_sud(self,sud):
		for row in sud:
			for num in row:
				print(str("" if num is None else str(num)).rjust(5),end='')
			print()

	def check(self,sud):
		numbers=[i for i in range(1,9+1)]

		#check rows
		for row in sud:
			self.assertEqual(sorted(row),numbers)

		#check columns
		for n_col in range(9):
			col=[sud[i][n_col] for i in range(9)]
			self.assertEqual(sorted(col),numbers)

		#check sub-squares
		for row in range(0,9,3):
			for col in range(0,9,3):
				nums=[]
				for i in range(3):
					for j in range(3):
						nums.append(sud[row+i][col+j])
				self.assertEqual(sorted(nums),numbers)

if __name__ == '__main__':
    unittest.main()


