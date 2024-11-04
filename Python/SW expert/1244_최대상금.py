def list_to_int(l):
    return int("".join(map(str,l)))

def max_value(number, k):
    global max_v
    max_v = 0

    def dfs(number_list, remained_change):
        global max_v
        if remained_change == 0:
            if list_to_int(number_list) > max_v:
                max_v = list_to_int(number_list)
            return
        
        for i in range(len(number_list)-1):
            for j in range(i+1, len(number_list)):
                number_list[i], number_list[j] = number_list[j], number_list[i]
                dfs(number_list, remained_change-1)
                number_list[i], number_list[j] = number_list[j], number_list[i]

    dfs(number,k)
    return max_v
        


n = int(input())
#print("case_num : ",n)
for test_case in range(n):
    number, count = input().split()
    number_list, count = list(map(int,number)), int(count)

    answer = max_value(number_list, count)    
    print(f"#{test_case+1} {answer}")
