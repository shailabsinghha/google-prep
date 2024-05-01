'''

possible subsets of a string

Using the input poutput method

input: ""   
output: "abc"

make the input smaller till it reaches 0


'''

possible_arr = set()

def all_subsets(output, inp):


	#base condition
	if(inp == ""):
		return

	# here we have 2 choices 
	# 1. take the inp
	# 2. do not take the inp

	possible_arr.add(output)
	possible_arr.add(output + inp[0])
	all_subsets(output+ inp[0], inp[1:])
	all_subsets(output, inp[1:])
	


all_subsets('', 'abc')
print(possible_arr)