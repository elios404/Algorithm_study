#컨베이어 벨트 위의 로봇
#벨트 회전부터 한다면 처음 로봇을 놓게 되는 것은 2번째 부터인가
#큰 중요한 점을 놓쳤다. 내구도 값 리스트는 들어오고 나가는 것 길이의 2배라는 점

from collections import deque

def checkRobotdrop(arr):
    if arr[n-1][1] == 1:
        arr[n-1][1] = 0
    return

def jumpRobot(arr, idx):
    if arr[idx][1] == 1 and arr[idx+1][1] == 0 and arr[idx+1][0] >= 1: #만약 idx칸에 로봇이 있고, 다음 칸이 로봇이 없고 내구도가 1 이상이라면
        arr[idx][1] = 0
        arr[idx+1][1] = 1
        arr[idx+1][0] -= 1
        if arr[idx+1][0] == 0:
            return 1
        return 0
    else:
        return 0

n,k = map(int, input().split())
a_list = list(map(int, input().split()))
front = deque([[a,0] for a in a_list[:n]])
back = deque([[a,0] for a in a_list[n:]])
check = 0
turn = 0

while(check < k):
    # process 1
    front_last = front.pop()
    back.appendleft(front_last)
    back_last = back.pop()
    front.appendleft(back_last)
    checkRobotdrop(front)

    #process 2
    for i in range(n-2,-1,-1):
        check += jumpRobot(front, i)
    checkRobotdrop(front)

    #process 3
    if front[0][0] >= 1:
        front[0][1] = 1
        front[0][0] -= 1
        if front[0][0] == 0:
            check += 1
    
    turn += 1

print(turn)