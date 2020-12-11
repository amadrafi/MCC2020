import math

T = 10
cases = [[13, 7, 0, -8, 1], [10, -7, -6, -6, 7], [9, 2, 5, -7, -6], [14, -4, 1, -10, -7], [6, -1, 2, -2, -8], [4, 7, -7, 8, -10], [7, -4, -8, 0, -5], [16, 9, 4, -3, -9], [5, -5, 3, 6, 4], [18, 4, -10, -9, -1]]
for i in range(T):
    moves = 0
    k = cases[i][0]
    x = cases[i][1]
    y = cases[i][2]
    a = cases[i][3]
    b = cases[i][4]

    dx = abs(a - x)
    dy = abs(b - y)
    # print(k ,dx, dy)

    while (dx != 0 and dy != 0) or moves < k:
        # 1,2
        if(dx == 1 and dy == 2):
            moves +=1
            dx =0
            dy = 0
        elif(dx == 2 and dy == 1):
            moves +=1
            dy = 0
            dx = 0
        # 1,5
        elif(dx == 5 and dy == 1):
            moves += 4
            dx = 0
            dy = 0
        elif(dx == 1 and dy == 5):
            moves +=4
            dx = 0
            dy = 0
        # 3,3
        elif(dx == 3 and dy == 3):
            moves +=2
            dx = 0
            dy = 0
        # 3,4
        elif(dx == 3 and dy == 4):
            moves +=3
            dx = 0
            dy = 0
        elif(dy == 3 and dx == 4):
            moves +=3
            dx = 0
            dy = 0
        # 1,3
        elif(dx == 3 and dy == 1):
            moves +=2
            dx = 0
            dy = 0
        elif(dy == 3 and dx == 1):
            moves +=2
            dx = 0
            dy = 0
        # 1,1
        elif(dy == 1 and dx == 1):
            moves +=2
            dx = 0
            dy = 0
        # 2,0
        elif(dy == 2 and dx == 0):
            moves +=2
            dx = 0
            dy = 0
        elif(dy == 0 and dx == 2):
            moves +=2
            dx = 0
            dy = 0
        elif(dy == 4 and dx == 0):
            moves +=2
            dx = 0
            dy = 0
        elif(dy == 0 and dx == 4):
            moves +=2
            dx = 0
            dy = 0
        # 1,0
        elif(dx == 0 and abs(dy) == 1):
            moves +=3
            dx = 0
            dy = 0
        elif(dy == 0 and abs(dx) == 1):
            moves +=3
            dx = 0
            dy = 0
        # 0,3
        elif(dx == 3 and dy == 0):
            moves +=3
            dx = 0
            dy = 0
        elif(dy == 3 and dx == 0):
            moves +=3
            dx = 0
            dy = 0
        # square = 8
        elif(dy == 2 and dy == 2):
            moves +=3
            dx = 0
            dy = 0
        # 2,2
        elif(dx == 2 and dy == 2):
            moves +=4
            dx = 0
            dy = 0
        # non-final
        elif(dx > dy):
            moves +=1
            dx -=2
            dy -=1
        elif(dy > dx):
            moves +=1
            dx -=1
            dy -=2
        elif(dy == dx):
            moves +=2
            dx -=3
            dy -=3
        if(dy < 0):
            dy = -dy
        if(dx < 0):
            dx = -dx
        # print(moves, dx,dy)
    if (moves <= k) and (dx == 0 and dy == 0) and ((k - moves ) % 2 == 0):
        print('YES')
    else:
        print('NO')
            