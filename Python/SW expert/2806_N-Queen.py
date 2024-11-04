#n*n 개의 격자에 n 개의 퀸을 서로 공격할 수 없게 놓는 방법의 수 n은 1<=n<=10
#첫 째 행을 돌면서 순환하고, 두 번째 열에서 빈 곳에 놓고, 이런 식으로 반복
def attack_range(grid,pos, mark):
    global n
    row_idx, col_idx = pos[0], pos[1]
    for i in range(n):
        if grid[row_idx][i] == -1:
            grid[row_idx][i] = mark
        if grid[i][col_idx] == -1:
            grid[i][col_idx] = mark
    for j in range(-n, n+1):
        if 0<= row_idx+j < n and 0<= col_idx+j < n and grid[row_idx+j][col_idx+j] == -1:
            grid[row_idx+j][col_idx+j] = mark
        if 0<= row_idx+j < n and 0<= col_idx-j < n and grid[row_idx+j][col_idx-j] == -1:
            grid[row_idx+j][col_idx-j] = mark
    
def return_back(grid,pos, mark):
    global n
    row_idx, col_idx = pos[0], pos[1]
    for i in range(n):
        if grid[row_idx][i] == mark:
            grid[row_idx][i] = -1
        if grid[i][col_idx] == mark:
            grid[i][col_idx] = -1
    for j in range(-n, n):
        if 0<= row_idx+j < n and 0<= col_idx+j < n and grid[row_idx+j][col_idx+j] == mark:
            grid[row_idx+j][col_idx+j] = -1
        if 0<= row_idx+j < n and 0<= col_idx-j < n and grid[row_idx+j][col_idx-j] == mark:
            grid[row_idx+j][col_idx-j] = -1

def find_case(grid, row):
    global n
    global answer
    if -1 not in grid[row]:
        return
    if row == n-1:
        for i in range(n):
            if grid[row][i] == -1:
                answer += 1
                return
    for i in range(n):
        if grid[row][i] == -1:
            attack_range(grid, (row, i), row)
            find_case(grid, row+1)
            return_back(grid, (row,i), row)


global n
global answer
t = int(input())
for test_case in range(t):
    n = int(input())
    answer = 0
    grid = [[-1]*n for _ in range(n)]

    find_case(grid,0)
    print(f"#{test_case+1} {answer}")
