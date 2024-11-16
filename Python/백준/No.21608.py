#상어 초등학교
global n

def findNearSit(p_sit, grid):
    global n
    x, y = p_sit
    dx = [-1,0,0,1]; dy = [0,-1,1,0] # 상, 좌, 우 ,하
    new_pos = []
    if grid != []:
        for i in range(4):
            new_x = x+dx[i]; new_y = y+dy[i]
            if 0<= new_x < n and 0<= new_y < n and grid[new_x][new_y] >= 0:
                new_pos.append((new_x, new_y))
    if grid == []:
        for i in range(4):
            new_x = x+dx[i]; new_y = y+dy[i]
            if 0<= new_x < n and 0<= new_y < n:
                new_pos.append((new_x, new_y))
    return new_pos

def searchMostEmptySit(sit_list, grid): #조건의 맞는 자리 중 가장 빈 자리가 많은 곳을 찾아줌
    global n
    max_num = 0
    max_sit = (n-1,n-1)
    if sit_list == []:
        for i in range(n):
            for j in range(n):
                if grid[i][j] > max_num:
                    max_num = grid[i][j]
                    max_sit = (i, j)
    elif sit_list != []:
        for s in sit_list:
            i,j = s[0],s[1]
            if grid[i][j] > max_num:
                max_num = grid[i][j]
                max_sit = (i,j)
            elif grid[i][j] == max_num:
                if i < max_sit[0]:
                    max_num = grid[i][j]
                    max_sit = (i,j)
                elif i == max_sit[0] and j < max_sit[1]:
                    max_num = grid[i][j]
                    max_sit = (i,j)
    return max_sit

n = int(input())
like = {}
for i in range(n*n):
    l = (list(map(int, input().split())))
    like[l[0]] = l[1:]
sit = {} # number = (x, y)
grid = [[0]*n for _ in range(n)] #근처의 빈자리 수를 저장
for i in range(n):
    for j in range(n):
        li = findNearSit((i,j), grid)
        grid[i][j] = len(li)
sitting = [[0]*n for _ in range(n)]

for p_num, p_like in like.items(): #int, list
    # process 1
    near_like_sit = {}
    for p in p_like:
        if p in sit:
            p_sit = sit[p] #좋아하는 사람 p 가 앉아있는 자리
            next_to_like = findNearSit(p_sit, grid) # list of tuples
            for next in next_to_like:
                if next not in near_like_sit : near_like_sit[next] = 1
                else : near_like_sit[next] += 1
    near_like_sit = sorted(near_like_sit.items(), key = lambda item: item[1], reverse = True) #list of tuple
    near_like_sit = [k[0] for k in near_like_sit if k[1] == near_like_sit[0][1]] #좋아하는 사람이 가장 많은 자리들
    #process 2
    can_sit = searchMostEmptySit(near_like_sit, grid)
    sit[p_num] = can_sit
    sitting[can_sit[0]][can_sit[1]] = p_num
    grid[can_sit[0]][can_sit[1]] = -1
    near_can_sit = findNearSit(can_sit, grid)
    for ncs in near_can_sit:
        grid[ncs[0]][ncs[1]] -= 1

for i in range(n):
    print(sitting[i])

def calculateScore(sitting, like):
    score = 0
    for i in range(n):
        for j in range(n):
            many = 0
            s = sitting[i][j]
            li = findNearSit((i,j),[])
            for l in li:
                if sitting[l[0]][l[1]] in like[s]:
                    many += 1
            if many == 0 : score += 0
            elif many == 1 : score += 1
            elif many == 2 : score += 10
            elif many == 3 : score += 100
            elif many == 4 : score += 1000
            #print(score)

    return score

print(calculateScore(sitting, like))