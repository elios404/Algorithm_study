#어떤 날짜에 대해서 상담을 할 수도 있고 안 할 수도 있다.
#만약 상담을 하기로 했다면, 상담이 종료된 날 이후 부터 다시 상담을 할 수 있고
#상담을 하지 않는다면 다음 날로 넘어갈 수 있다.

#상담을 안하고 다음으로 넘어가는 경우를 앞쪽에 작성했다. 특정한 조건문에 영향 받는 것을 막기 위해서

global answer

def check_income(info, day, income):
    global answer
    if day >= len(info):
        answer = max(answer, income)
        return
    check_income(info, day+1, income) #상담 안하고 다음으로 넘어가는 경우
    
    add_income = income + info[day][1]
    next_day = day + info[day][0]
    if next_day > len(info): #상담 종료일이 퇴사 일 이후라면
        answer = max(answer, income) 
        return
    elif next_day == len(info): #상담 종료일이 퇴사 일 이라면
        answer = max(answer, add_income) #현재 상담까지는 할 수 있음
        return
    check_income(info, next_day, add_income)
    
n = int(input())
info = []
answer = 0
for i in range(n):
    day, income = map(int,input().split())
    info.append([day,income])
check_income(info, 0, 0)

print(answer)