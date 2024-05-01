'''

Maximum sum of constigous sub array since there camn be negative numbers as well


'''

import math

def kadane(arr):

	_max = -math.inf
	
	curr_max = arr[0]
	for i in arr[1:]:

		curr_max = max(curr_max+ i, curr_max)
		_max=max(_max, curr_max)

	return _max

print(kadane([-2, 1, 4, -1, -2, -1, 5, -3]))