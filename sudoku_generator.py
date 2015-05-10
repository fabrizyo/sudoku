from itertools import permutations
from copy import copy
from random import shuffle
from random import choice

def get_nums():
	return [i for i in range(1,9+1)]

'''
	return a matrix 9x9 Sudoku

	remove:
		 delete randomly remove numbers (set to None) from matrix
'''
def get_random_sudoku(remove=0):
	can_rows={i:set(get_nums()) for i in range(9)}
	can_cols={i:set(get_nums()) for i in range(9)}
	can_squa={i:set(get_nums()) for i in range(9)}
	curr=[[None]*9 for i in range(9)]
	res=get_random(curr,can_rows,can_cols,can_squa,0)
	choices=[i for i in range(9*9)]
	for i in range(remove):
		index=choice(choices)
		choices.remove(index)
		curr[index//9][index%9]=None
	return curr


def get_random(curr,can_rows,can_cols,can_squa,index):
	if index==9*9:
		return copy(curr)

	row=index//9
	col=index%9
	squ=(col//3)+(row-row%3)

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

		res=get_random(curr,can_rows,can_cols,can_squa,index+1)
		if res is not None:
			return res

		can_rows[row].add(num)
		can_cols[col].add(num)
		can_squa[squ].add(num)
	return None


