# 문제 뱀
# 문제를 제대로 읽지 않아서 헤맨 부분이 있다. 문제에서는 시작지점을 1,1로 나는 0,0으로 설정했고
# 몇 초 뒤 방향 전환도 몇초에 도달하면 전환하는게 아니라 몇 초가 끝나고 방향을 전환하는 식이다.

def check_game_end(y,x,n):
    global grid
    if y >= n or y < 0 or x >= n or x < 0:
        return True
    elif grid[y][x] == 2:
        return True
    else:
        return False

from collections import deque

N = int(input())
K = int(input())

grid = [[0]*N for _ in range(N)]

for _ in range(K):
    y,x = map(int,input().split())
    grid[y-1][x-1] = 1 # if there is apple 1, if not 0

L = int(input())
move = {}
now_direction = 0

for _ in range(L):
    sec, direction = input().split()
    sec = int(sec)
    if direction == "D":
        add = 1
    else:
        add = -1
    move[sec] = add
    

y,x = 0,0
# 우측 0, 아래 1, 좌측 2, 위 3
dy = [0,1,0,-1]
dx = [1,0,-1,0]
now = 0
length = 1
snake = deque()
snake.append((0,0))
grid[0][0] == 2
time_pass = 0

while True:
    if time_pass in move:
        change_dir = move[time_pass]
        now = (now+change_dir)%4
    time_pass += 1
    ny,nx = y+dy[now], x+dx[now]
    #print(f"# {time_pass}",ny, nx)
    if check_game_end(ny,nx,N):
        break
    elif grid[ny][nx] == 1:
        length += 1

    y,x = ny,nx
    grid[y][x] = 2
    snake.append((y,x))
    while len(snake) > length:
        delete = snake.popleft()
        grid[delete[0]][delete[1]] = 0

print(time_pass)