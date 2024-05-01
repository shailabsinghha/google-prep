'''

According to moore voting the possible candidate will appear for atleat 2 time
continously if that element appears median times
the given element 

'''

def moore(arr):

	candidate= arr[0]

	# this keep record of the nuber of times a value appears continuously

	count =0
	for i in arr[1:]:
		
		if count==0:
			candidate=i
			count+=1

		elif candidate==i:
			count+=1

		else:

			count-=1

	return candidate

print(moore([2, 3, 2, 4,2,  5, 6, 2, 1, 2])) 