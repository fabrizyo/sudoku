from itertools import permutations
from copy import copy
from random import shuffle

def get_all_sudokus(n):
	curr=[[None]*n for i in range(n)]
	return get_suds(n,curr,0)

def get_random_sudoku(n):
	curr=[[None]*n for i in range(n)]
	return get_suds(n,curr,0,True)[0]

def get_permutations(l,is_random):
	if is_random:
		l=l[:]
		shuffle(l)
	return permutations(l)

def get_suds(n,curr,index,is_random=False):
	if index==n:
		return [copy(curr)]

	res=[]
	#vertical
	poss_v=set([i for i in range(1,n+1)])
	if index!=0:
		poss_v-=set([curr[row][index] for row in range(index)])
	poss_v=sorted(list(poss_v))

	perms_v=get_permutations(poss_v,is_random)
	for perm_v in perms_v:

		if index!=0:
			found=True
			for row in range(index,n):
				if perm_v[row-index] in curr[row][:index]:
					found=False
					break
			if not found:
				continue

		#found
		#place vertical
		for i in range(index,n):
			curr[i][index]=perm_v[i-index]

		#check horizontal
		poss_h=set([i for i in range(1,n+1)])
		poss_h-=set(curr[index][:index+1])
		poss_h=sorted(list(poss_h))

		perms_h=get_permutations(poss_h,is_random)
		for perm_h in perms_h:

			if index!=0:
				found=True
				for col in range(index+1,n):
					for row in range(index):
						if perm_h[col-(index+1)]==curr[row][col]:
							found=False
							break
					if not found:
						break
				if not found:
					continue

			#found
			#place horizontal
			for i in range(index+1,n):
				curr[index][i]=perm_h[i-(index+1)]

			res.extend(get_suds(n,curr,index+1,is_random))
			if len(res)!=0 and is_random:
				return res
	return res


