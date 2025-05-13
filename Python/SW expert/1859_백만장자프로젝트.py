T = int(input())

for test_case in range(1, T+1):
    input_count = int(input())
    input_list = list(map(int,input().split()))
    input_list.reverse()
    max_price = 0
    count = 0
    reward = 0
    isum = 0
    for i in input_list:
        if i > max_price:
            reward += (max_price * count) - isum
            max_price = i
            count = 0
            isum = 0
        else:
            count += 1
            isum += i
    reward += (max_price * count) - isum
    print(f"#{test_case} {reward}")