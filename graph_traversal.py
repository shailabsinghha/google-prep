am = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
visited = set()

def dfs(am, node):

	if(node not in visited):
		print(node , end= " ")
		visited.add(node)
		# dfs in all neighbours
		if(node in am):
			for i in am[node]:
				dfs(am, i)


def bfs(am, node):

	_visited = []
	q = []

	q.append(node)
	_visited.append(node)
	# considering that this first node will have some ending
	while q:

		print(q[0], end= " ")
		el = q.pop(0) # pop the firs element
		if(el in am):
			for _ in am[el]:

				if _ not in _visited:
					q.append(_)
					_visited.append(_)




dfs(am, '5')
print("\n")
bfs(am, '5') 