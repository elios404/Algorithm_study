#깊이우선, 혹은 너비 우선으로 경로가 이어지는 지 확인하는 문제

from collections import deque

def find_route(start, end):
    global grid
    been = [[False] * 16 for _ in range(16)]
    next_block = deque()
    next_block.append(start)

    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    while next_block:
        pos = next_block.popleft()
        y,x = pos[0], pos[1]
        been[y][x] = True

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if  ny >=0  and ny < 16 and nx >= 0 and nx < 16 and grid[ny][nx] != 1 and been[ny][nx] == False:
                if (ny,nx) == end:
                    return True
                next_block.append((ny,nx))
    return False

for _ in range(1,11):
    test_case = int(input())
    grid = []
    for _ in range(16):
        row = list(input())
        row = list(map(int, row))
        grid.append(row)
    for i in range(16):
        for j in range(16):
            if grid[i][j] == 2:
                start = (i,j)
            elif grid[i][j] == 3:
                end = (i,j)
    
    if find_route(start, end):
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")