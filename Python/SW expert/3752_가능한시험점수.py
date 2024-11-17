# 이 문제는 어떤 문제가 맞았는지 틀렸는지 2가지 경우로 나누어서 재귀함수를 호출하는 방식으로 풀면 될 듯
# 재귀함수를 여러번 호출하니 제한시간 초과가 발생했다. 아마 ssafy는 재귀함수 호출에 조금 더 까다로울 수도?
# 그렇다면 최대한 하나의 함수에서 풀 수 있도록 하는 것이 좋겠다. --> 보급로 문제에서도 DFS나 BFS 보다 heapq를 이용하여
# 하나의 함수에서 처리했다.

test_num = int(input())

for T in range(test_num):
    n = int(input())
    score_list = list(map(int, input().split()))
    cand = {0}
    count = {}
    for s in score_list:
        if s not in count : count[s] = 1
        else : count[s] += 1
    count_list = sorted(count.items(), key = lambda item : item[0]) #(key, value)
    
    for prob_score, prob_num in count_list:
        cand_list = list(cand)
        #print(f"cans_list {cand_list}")
        for cand_mem in cand_list:
            for i in range(prob_num+1):
                cand.add(cand_mem + prob_score*i)
        #print(f"cand : {cand}")
    
    print(f"#{T+1} {len(cand)}")