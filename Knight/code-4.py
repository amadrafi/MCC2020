# Python3 code to find minimum steps to reach 
# to specific cell in minimum moves by Knight 
class cell: 
	
	def __init__(self, x = 0, y = 0, dist = 0): 
		self.x = x 
		self.y = y 
		self.dist = dist 
		
# checks whether given position is 
# inside the board 
def isInside(x, y, N): 
	if (x >= 1 and x <= N and
		y >= 1 and y <= N): 
		return True
	return False
	
# Method returns minimum step to reach 
# target position 
def minStepToReachTarget(knightpos, 
						targetpos, N): 
	
	# all possible movments for the knight 
	dx = [2, 2, -2, -2, 1, 1, -1, -1] 
	dy = [1, -1, 1, -1, 2, -2, 2, -2] 
	
	queue = [] 
	
	# push starting position of knight 
	# with 0 distance 
	queue.append(cell(knightpos[0], knightpos[1], 0)) 
	
	# make all cell unvisited 
	visited = [[False for i in range(N + 1)] 
					for j in range(N + 1)] 
	
	# visit starting state 
	visited[knightpos[0]][knightpos[1]] = True
	
	# loop untill we have one element in queue 
	while(len(queue) > 0): 
		
		t = queue[0] 
		queue.pop(0) 
		
		# if current cell is equal to target 
		# cell, return its distance 
		if(t.x == targetpos[0] and
		t.y == targetpos[1]): 
			return t.dist 
			
		# iterate for all reachable states 
		for i in range(8): 
			
			x = t.x + dx[i] 
			y = t.y + dy[i] 
			
			if(isInside(x, y, N) and not visited[x][y]): 
				visited[x][y] = True
				queue.append(cell(x, y, t.dist + 1)) 

# Driver Code	 
T = 10
cases = [[21, -5, -6, 6, 7], [5, 3, 7, 4, -3], [13, 6, -7, -9, -6], [6, 1, 1, -4, -6], [9, 5, -6, 0, 6], [8, -8, 2, 6, 4], [4, 3, -3, 5, 4], [4, 3, -2, 0, 3], [0, -5, -7, -5, -9], [4, 3, 4, 0, 7]]

for i in range(T):
    k = cases[i][0]
    x = cases[i][1]
    y = cases[i][2]
    a = cases[i][3]
    b = cases[i][4]
    N = 2000
    knightpos = [x, y] 
    targetpos = [a, b] 
    step = minStepToReachTarget(knightpos, targetpos, N)
    if step == None:
        print("NO")
    elif step != k:
        print("NO")
    elif step > k:
        if (step - k) % 2 == 0:
            print("YES")
    else:
        print("YES")
	
# This code is contributed by 
# Kaustav kumar Chanda 
