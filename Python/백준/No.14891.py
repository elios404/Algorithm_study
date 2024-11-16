#톱니바퀴 문제
#톱니를 큐로 처리하고 큐 값을 비교하여 앞 뒤를 빼고 더하면 될 것 같다.

from collections import deque

def turnGearbyDirection(gear, d):
    if d == 1:
        temp = gear.pop()
        gear.appendleft(temp)
    elif d == -1:
        temp = gear.popleft()
        gear.append(temp)
    return gear
def checkRight(gears,gear_num):
    connect1 = gears[gear_num][2]
    connect2 = gears[gear_num+1][6]
    if connect1 != connect2:
        return True
    else: False

def checkLeft(gears, gear_num):
    connect1 = gears[gear_num][6]
    connect2 = gears[gear_num-1][2]
    if connect1 != connect2:
        return True
    else:
        False

def turnGear(gears, gear_num, d, turned):
    turned.add(gear_num)
    #print("turn gear : ", gear_num)
    if gear_num == 0:
        if checkRight(gears, gear_num) and gear_num+1 not in turned:
            turnGear(gears, gear_num+1, -d, turned)
        gears[gear_num] = turnGearbyDirection(gears[gear_num], d)
    elif gear_num == 3:
        if checkLeft(gears, gear_num) and gear_num-1 not in turned:
            turnGear(gears, gear_num-1, -d, turned)
        gears[gear_num] = turnGearbyDirection(gears[gear_num], d)
    else: #gear_num = 2 or 3
        if checkRight(gears, gear_num) and gear_num+1 not in turned:
            turnGear(gears, gear_num+1, -d, turned)
        if checkLeft(gears, gear_num) and gear_num-1 not in turned:
            turnGear(gears,gear_num-1, -d, turned)
        gears[gear_num] = turnGearbyDirection(gears[gear_num], d)
    return

gears =[]
for i in range(4):
    values = input()
    values_list = list(c for c in values)
    gears.append(deque(values_list))

k = int(input())

for T in range(k):
    gear_num, d = map(int, input().split())
    turned = set()
    turnGear(gears, gear_num-1, d, turned)

answer = 0
for i in range(4):
    if gears[i][0] == '1' : answer += (2**i)
print(answer)