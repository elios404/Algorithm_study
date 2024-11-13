#연산자 끼워넣기 문제
#브루트 포스 문제 -->  연산자의 조합을 어떻게 짤 것인가

global max_answer, min_answer

def cal(num_list, operator, result, idx):
    global max_answer, min_answer
    if idx == len(num_list): #끝 숫자까지 다 탐색함.
        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)
        return
    
    b = num_list[idx]

    for i in range(len(operator)):
        op = operator[i]
        if op != 0: #연산자 사용 횟수가 남아있다면
            if i == 0: #plus
                operator[i] -= 1
                cal(num_list, operator, result+b, idx+1)
                operator[i] += 1
            elif i == 1: #minus
                operator[i] -= 1
                cal(num_list, operator, result-b, idx+1)
                operator[i] += 1
            elif i == 2: #multiple
                operator[i] -= 1
                cal(num_list, operator, result*b, idx+1)
                operator[i] += 1
            elif i == 3: #divide
                operator[i] -= 1
                if result >= 0:
                    temp = result//b
                else: #result < 0
                    temp = -((-result)//b)
                cal(num_list, operator, temp, idx+1)
                operator[i] += 1
    return

n = int(input())
num_list = list(map(int,input().split()))
operator = list(map(int, input().split()))

max_answer, min_answer = -(10**9), 10**9

cal(num_list, operator, num_list[0], 1)
print(max_answer)
print(min_answer)