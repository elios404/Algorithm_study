#모든 조합을 만들어 보고 칼로리를 넘지 않는 선에서 점수가 최대인 것을 찾아야 한다.
#그럼 모든 조합을 어떻게 찾아보지? --> 몇 개로 조합을 만들지도 정해지지 않음.
#이거 깊이 우선 탐색으로 해야할 것 같은데?

global max_score, limit, length, food_list

def find_comb(idx, calory, score):
    global max_score, limit, length, food_list
    calory += food_list[idx][1]
    if calory > limit or idx == length-1:
        max_score = max(max_score, score)
        return
    score += food_list[idx][0]
    for i in range(idx+1, length):
        find_comb(i, calory, score)

T  = int(input())
for test_case in range(T):
    n, limit = map(int, input().split())
    food_list = [] #score, calories
    for i in range(n):
        score, calory = map(int, input().split())
        food_list.append([score, calory])
    
    food_list.sort(key = lambda x:x[1])
    max_score = 0
    length = len(food_list)

    for k in range(length):
        find_comb(k, 0, 0)
    
    print(f"#{test_case+1} {max_score}")