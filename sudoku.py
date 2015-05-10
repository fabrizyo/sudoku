from copy import copy
from random import shuffle
from random import choice


def get_indexes(index):
	row=index//9
	col=index%9
	squ=(col//3)+(row-row%3)
	return row,col,squ

def get_cans(curr):
	can_rows={i:set(get_nums()) for i in range(9)}
	can_cols={i:set(get_nums()) for i in range(9)}
	can_squa={i:set(get_nums()) for i in range(9)}

	for index in range(9*9):
		row,col,squ=get_indexes(index)
		num=curr[row][col]
		if num is not None:
			can_rows[row].discard(num)
			can_cols[col].discard(num)
			can_squa[squ].discard(num)

	return can_rows,can_cols,can_squa	

def get_nums():
	return [i for i in range(1,9+1)]

'''
	Solve sudoku
	sud:
		a matrix 9x9 Sudoku to solve, use None for empty cells
'''
def solve_sudoku(sud):
	curr=copy(sud)
	can_rows,can_cols,can_squa=get_cans(curr)
	return solve(curr,can_rows,can_cols,can_squa,0)

'''
	return a matrix 9x9 Sudoku

	remove:
		 delete randomly remove numbers (set to None) from matrix
'''
def get_random_sudoku(remove=0):
	curr=[[None]*9 for i in range(9)]
	can_rows,can_cols,can_squa=get_cans(curr)
	res=solve(curr,can_rows,can_cols,can_squa,0)

	choices=[i for i in range(9*9)]
	for i in range(remove):
		index=choice(choices)
		choices.remove(index)
		row,col,squ=get_indexes(index)
		curr[row][col]=None
	return curr


def solve(curr,can_rows,can_cols,can_squa,index):
	if index==9*9:
		return copy(curr)

	row,col,squ=get_indexes(index)
	if curr[row][col] is not None:
		return solve(curr,can_rows,can_cols,can_squa,index+1)		

	can=set(get_nums())
	can&=can_rows[row]
	can&=can_cols[col]
	can&=can_squa[squ]

	can=list(can)
	shuffle(can) #random
	for num in can:
		curr[row][col]=num
		can_rows[row].remove(num)
		can_cols[col].remove(num)
		can_squa[squ].remove(num)

		res=solve(curr,can_rows,can_cols,can_squa,index+1)
		if res is not None:
			return res

		curr[row][col]=None
		can_rows[row].add(num)
		can_cols[col].add(num)
		can_squa[squ].add(num)
	return None


