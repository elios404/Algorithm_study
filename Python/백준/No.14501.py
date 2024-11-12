#이건 직접 상담했을 경우를 확인해야 한다.

global answer

def check_income(info, day, income):
    global answer
    add_income = income + info[day][1]
    next_day = day + info[day][0]
    if next_day > len(info):
        answer = max(answer, income)
        return
    elif next_day == len(info):
        answer = max(answer, add_income)
        return
    elif day == len(info):
        answer = max(answer,income)
        return
    check_income(info, next_day, add_income)
    check_income(info, day+1, income)

n = int(input())
info = []
answer = 0
for i in range(n):
    day, income = map(int,input().split())
    info.append([day,income])
check_income(info, 0, 0)

print(answer)