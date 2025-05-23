#dfs 문제, 목적지 까지 가는 가장 짧은 경로를 찾아야함.
#몰라서 샘플 코드를 확인함. dfs로 푸는 것이 아님 BFS로 푸는 것
#이때 상하좌우를 다 확인하는데, 이동하려는 상하좌우 cost에 대해서 현재 담고있는 cost 보다 작을 때에만 새로 확인하는 걸로 넣음
#float('inf') 가 있으면 좋을 듯

from collections import deque

def bfs_search():
    global grid, time, row

    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    next_move = deque()
    next_move.append((0,0))

    while next_move:
        pos = next_move.popleft()
        y,x = pos[0], pos[1]
        length = time[y][x]
        for i in range(4):
            ny, nx = y+dy[i],x+dx[i]
            if ny < row and ny >= 0 and nx < row and nx >= 0:
                if time[ny][nx] > length + grid[ny][nx]:
                    time[ny][nx] = length + grid[ny][nx]
                    next_move.append((ny,nx))
    
    return time[row-1][row-1]

T = int(input())

for test_case in range(1,T+1):
    grid = []
    row = int(input())
    for _ in range(row):
        row_list = list(input())
        row_list = list(map(int, row_list))
        grid.append(row_list)
    
    time = [[float('inf')] * row for _ in range(row)]
    time[0][0] = grid[0][0]
    
    answer = bfs_search()
    print(f"#{test_case} {answer}")


#-------- 2가지 코드로 풀음 ------ 아래는 예전 코드

from heapq import heappop, heappush

def findRoute(arr, cost):
    dy = [-1,0,1,0]; dx = [0,-1,0,1]
    pq = [(arr[0][0], 0,0)]
    n = len(arr[0])
    while(pq):
        now_cost, y, x = heappop(pq)
        if (y,x) == (n-1,n-1):
            return now_cost + arr[y][x]
        next_move = [(y + dy[i], x + dx[i]) for i in range(4)]

        for move in next_move:
            if 0<= move[0] < n and 0 <= move[1] < n: #격자 안에 있다면
                move_cost = now_cost + arr[move[0]][move[1]]
                if move_cost < cost[move[0]][move[1]]:
                    cost[move[0]][move[1]] = move_cost
                    heappush(pq, (move_cost,move[0], move[1]))


test_num = int(input())

for T in range(test_num):
    n = int(input())
    arr = []
    for i in range(n):
        l = input()
        li = [int(c) for c in l]
        arr.append(li)
    cost = [[float('inf')]*n for _ in range(n)]

    print(f"#{T+1} {findRoute(arr, cost)}")