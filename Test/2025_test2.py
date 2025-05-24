#문제이름 : 원형
# 원 위에 m개의 칸이 있고 n이 주어진다. 앞으로 입력된 n개의 숫자에 대해서 그 숫자들을 순회해야한다.
#이때 이동은 반드시 시계방향으로 한다. 만약 노드 중 하나를 제거하는 상황에서 이동하는 거리가 최소가 되는 거리는 얼마인가?
#전부 탐색을 해야하고, 시간복잡도가 크니 이를 줄여야 한다.

T = int(input())

for test_case in range(1,T+1):
    N,M = map(int, input().split())
    node = list(map(int,input().split()))

    total_length = 0
    for i in range(len(node)-1):
        length = node[i+1] - node[i]
        if length < 0:
            length = M+length
        total_length += length
    
    first_length = node[1] - node[0]
    if first_length < 0:
        first_length = M+first_length
    min_length = total_length - first_length

    for i in range(1,len(node)-1):
        length1 = node[i] - node[i-1]
        length2 = node[i+1] - node[i]
        length3 = node[i+1] - node[i-1]
        if length1 < 0:
            length1 = M+length1
        if length2 < 0:
            length2 = M+length2
        if length3 < 0:
            length3 = M+length3
        
        cand_length = total_length - length1 - length2 + length3
        min_length = min(min_length, cand_length)
    
    last_length = node[-1] - node[-2]
    if last_length < 0:
        last_length = M+last_length
    min_length = min(min_length, total_length-last_length)

    print(f"#{test_case} {min_length}")