# 전부 순환하는 것이 아니라 1~5까지 빼고 다시 사이클 시작, 숫자는 8자리 이니 계속 위치 별로 빼는 숫자가 변한다.

from collections import deque

for T in range(10):
    test_num = int(input())
    code = deque(map(int,input().split()))
    
    minus = 1
    b = True
    while(b):
        num = code.popleft()
        num -= minus
        if num <= 0:
            num = 0
            b = False
        code.append(num)
        minus += 1
        if minus == 6: minus = 1
    print(f"#{test_num}", end=" ")
    for n in code:
        print(n, end=" ")
    print()