# 문제의 핵심은 격자가 주어졌을 때 가운데 마름모 부분의 값을 읽는 것

test_num = int(input())

for T in range(test_num):
    n = int(input())
    answer = 0
    farm = []
    for i in range(n):
        val = input()
        r = [int(c) for c in val]
        farm.append(r)
    
    mid = n//2
    side = list(range(mid+1)) + list(range(mid-1,-1,-1))
    #print(side)
    for idx, s in enumerate(side):
        r = farm[idx][mid-s:mid+s+1]
        #print(r)
        answer += sum(r)
    
    print(f"#{T+1} {answer}")