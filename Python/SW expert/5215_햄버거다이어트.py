T  = int(input())
for test_case in range(T):
    n, calories = map(int, input().split())
    prod_list = [] #score, calories
    for i in range(n):
        score, calory = map(int, input().split())
        prod_list.append([score, calory])
    
    prod_list.sort(key = lambda x:x[1], reverse=True)
    #print(prod_list)
    
    answer = 0
    for idx, prod in enumerate(prod_list):
        score = prod[0]
        sum_cal = prod[1]
        if idx !=  n-1:
            for j in range(idx+1, n):
                if sum_cal + prod_list[j][1] <= calories:
                    score += prod_list[j][0]
                    sum_cal += prod_list[j][1]
                else:
                    break
        answer = max(answer, score)
    print(f"#{test_case+1} {answer}")
