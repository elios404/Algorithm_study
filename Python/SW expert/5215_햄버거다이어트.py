#최대한 많은 재료가 들어가는게 꼭 좋지는 않다. 칼로리 대비 점수가 일정한 것이 아니기에
#조합을 완전 탐색으로 해 봐야 할까?
#재료를 순서대로 넣는다 안 넣는다로 하고 칼로리가 넘는지 확인

def make_combination(food_idx, score, calory):
    global food_num, limit_calory, food_score, food_calory
    if food_idx == food_num:
        return score
    if calory + food_calory[food_idx] > limit_calory: #재료를 추가했을 때 칼로리가 넘친다면
        new_score = make_combination(food_idx+1, score, calory) #idx번쨰 재료 추가하지 않은 경우
        return max(new_score, score)
    else: #재료를 추가해도 괜찮다면
        new_score1 = make_combination(food_idx+1, score+food_score[food_idx], calory+food_calory[food_idx]) #idx 번째 재료를 추가한 경우
        new_score2 = make_combination(food_idx+1, score, calory) #idx번쨰 재료 추가하지 않은 경우
        new_score = max(new_score1, new_score2)
        return max(new_score, score)

T = int(input())
for test_case in range(1, T+1):
    food_num, limit_calory = map(int, input().split())
    food_score = list()
    food_calory = list()
    max_score = 0
    for _ in range(food_num):
        temp_score, temp_calory = map(int, input().split())
        food_score.append(temp_score)
        food_calory.append(temp_calory)
    print(f"#{test_case} {make_combination(0,0,0)}")