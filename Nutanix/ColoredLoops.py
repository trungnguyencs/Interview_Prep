# https://leetcode.com/discuss/interview-question/417125/Nutanix-or-OA-Summer-Intern-2020-or-Colored-Loops-and-Grumpy-Shopkeeper

matrix = [['A','A','A','A'], \
		['A','B','C','A'], \
		['A','A','K','R']]

# visited = set()
def colored_loops(matrix):
	global visited 
	visited_colors = set()
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] not in visited_colors:
				val = matrix[i][j]
				# visited = set()
				if dfs(matrix, i, j, val, set(), (None, None)):
					return True
	return False

def dfs(matrix, i, j, val, visited, parent):
	# global visited
	visited.add((i,j))
	neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
	for neighbor in neighbors:
		x, y = neighbor
		if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == val:
			if neighbor in visited and neighbor != parent:
				return True
			elif neighbor not in visited:
				dfs(matrix, x, y, val, visited, (i,j))
	# print(str((i,j)) + ' ' + str(parent))

print(colored_loops(matrix))

