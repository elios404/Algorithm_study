#청소하는 칸의 갯수를 세는 것 --> 0의 갯수를 세는 것고 뭐가 다르지?

d_list = [[-1,0],[0,1],[1,0],[0,-1]]

n,m = map(int, input().split())
x,y,d = map(int, input().split())
arr = []
answer = 0


for i in range(n):
    r = list(map(int, input().split()))
    arr.append(r)

while(True):
    if arr[x][y] == 0:
        arr[x][y] = 2
        answer += 1
    elif arr[x-1][y] != 0 and arr[x+1][y] != 0 and arr[x][y-1] != 0 and arr[x][y+1] != 0:
        x, y = x-d_list[d][0], y-d_list[d][1]
        if arr[x][y] == 1:
            break
    else:
        d = (d-1)%4 
        if arr[x+d_list[d][0]][y+d_list[d][1]] == 0:
            x,y = x+d_list[d][0], y+d_list[d][1]

print(answer)