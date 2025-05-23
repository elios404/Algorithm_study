from collections import deque

def find_bomb_near():
    global size, grid, check
    is_bomb_grid = [[False]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if grid[i][j] == "*":
                check[i][j] = True
                for a in range(-1,2):
                    for b in range(-1,2):
                        ni, nj = i+a, j+b
                        if ni >= 0 and ni < size and nj >= 0 and nj < size:
                            is_bomb_grid[ni][nj] = True
    return is_bomb_grid

def find_bomb():
    global size, grid, check  
    answer = 0 
    is_bomb_grid = find_bomb_near()

    dy = [-1,-1,-1,0,0,1,1,1]
    dx = [-1,0,1,-1,1,-1,0,1]

    #먼저 주변에 지뢰가 없는 칸들을 제거
    for i in range(size):
        for j in range(size):
            if is_bomb_grid[i][j] == False and check[i][j] == False:
                answer += 1
                near = deque()
                near.append((i,j))
                while near:
                    pos = near.popleft()
                    y,x = pos[0], pos[1]
                    check[y][x] = True
                    for k in range(8):
                        ny, nx = y+dy[k], x+dx[k]
                        if ny>=0 and ny<size and nx>=0 and nx<size:
                            if is_bomb_grid[ny][nx] == False and check[ny][nx] == False:
                                near.append((ny,nx))
                            check[ny][nx] = True

    #나머지 한 칸 씩만 남은 것들 제거
    for i in range(size):
        for j in range(size):
            if check[i][j] == False:
                answer += 1
    return answer
    
                
T = int(input())

for test_case in range(1,T+1):
    size = int(input())
    grid = []
    for _ in range(size):
        row = list(input())
        grid.append(row)

    check = [[False]*size for _ in range(size)]
    ans = find_bomb()
    print(f"#{test_case} {ans}")