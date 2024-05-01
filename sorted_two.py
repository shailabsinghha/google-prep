'''
	Sorting 2 given sorted arrays

	1. Using  a binary search tree to insert the values by iterating into the arrays 
		- Max Space utilized will be O(n+ m+ ...)

	2. Store the frequency as well if there are multiple same values
	3. Time complexity will be O(nlogn) + O(mlogm) +... 

'''


import bisect as bt

# this question is intended for 2 arrays/ list only
def _sort(arr1, arr2):
	
	sorted_list = []

	for i in arr1:
		bt.insort(sorted_list, i)

	for i in arr2:
		bt.insort(sorted_list, i)

	return sorted_list


print(_sort([3,2, 4, 7 ,0, 12], [13,2, 14, 7 ,10, 22]))