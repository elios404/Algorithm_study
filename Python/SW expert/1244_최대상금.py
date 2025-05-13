#문제 해결 못함. 아래 코드는 제대로 작동하지 않음
#DFS를 통한 완전 탐색으로 문제를 해결해야 한다. 

T = int(input())

for test_case in range(1, T+1):
    input_nums = list(input().split())
    number, count = input_nums[0], int(input_nums[1]) #string, int
    number_list = list(map(int,number))
    sorted_number_list = sorted(number_list, reverse=True)
    print(f"answer : {sorted_number_list}")
    
    for i in range(len(number_list)):
        if count == 0 or number_list == sorted_number_list:
            break
        for j in range(len(number_list)-1, i-1, -1):
            if number_list[j] == sorted_number_list[i]:
                temp = number_list[j]
                number_list[j] = number_list[i]
                number_list[i] = temp
                break
        count -= 1

    while(count != 0):
        temp = number_list[-1]
        number_list[-1] = number_list[-2]
        number_list[-2] = temp
        count -= 1

    answer = int("".join(map(str,number_list)))
    print(f"#{test_case} {answer}")
