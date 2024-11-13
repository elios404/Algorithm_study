#시험 감독 문제

import math

n = int(input())
a_list = list(map(int, input().split()))
b,c = map(int, input().split())
answer = 0

for a in a_list:
    answer += 1
    if a < b:
        continue
    else:
        more = a-b
        need = math.ceil(more/c)
        answer += need

print(answer)