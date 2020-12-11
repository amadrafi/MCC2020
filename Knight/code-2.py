# Python3 code to find minimum steps to reach 
# to specific cell in minimum moves by Knight 
class cell: 
	def __init__(self, x = 0, y = 0, dist = 0): 
		self.x = x 
		self.y = y 
		self.dist = dist 
def isInside(x, y, N): 
	if (x >= 1 and x <= N and
		y >= 1 and y <= N): 
		return True
	return False
def minStepToReachTarget(knightpos, 
						targetpos, N): 
	dx = [2, 2, -2, -2, 1, 1, -1, -1] 
	dy = [1, -1, 1, -1, 2, -2, 2, -2] 
	
	queue = [] 
	queue.append(cell(knightpos[0], knightpos[1], 0))
	visited = [[False for i in range(N + 1)] 
					for j in range(N + 1)] 
	
	visited[knightpos[0]][knightpos[1]] = True
	while(len(queue) > 0): 
		
		t = queue[0] 
		queue.pop(0) 
		if(t.x == targetpos[0] and
		t.y == targetpos[1]): 
			return t.dist 
		for i in range(8): 
			
			x = t.x + dx[i] 
			y = t.y + dy[i] 
			
			if(isInside(x, y, N) and not visited[x][y]): 
				visited[x][y] = True
				queue.append(cell(x, y, t.dist + 1)) 

T = 10
cases = [[21, -5, -6, 6, 7], [5, 3, 7, 4, -3], [13, 6, -7, -9, -6], [6, 1, 1, -4, -6], [9, 5, -6, 0, 6], [8, -8, 2, 6, 4], [4, 3, -3, 5, 4], [4, 3, -2, 0, 3], [0, -5, -7, -5, -9], [4, 3, 4, 0, 7]]

minstep = 0
for i in range(T):
	k = cases[i][0]
	x = cases[i][1]
	y = cases[i][2]
	a = cases[i][3]
	b = cases[i][4]

	knightpos = [x, y]
	targetpos = [a, b]
	minstep = minStepToReachTarget(knightpos, targetpos, 10000)
	if minstep == None:
		print("NO")
	elif minstep <= k:
		if (k - minstep) % 2 == 0:
			print("YES")
		else:
			print("NO")
	else:
		print("YES") 