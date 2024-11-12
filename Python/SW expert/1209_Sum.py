# 총 10,000개의 격자를 확인해야 한다.
# 대각선의 경우 (i, i) 형태이거나 (99-i, i) 형태여야 한다.

for test_num in range(10):
    test_case = int(input())
    num_list = [list(map(int, input().split())) for _ in range(100)]
    #grid = [num_list[i*100:i*100+100] for i in range(10)]
    row_sum, col_sum = [0]*100, [0]*100
    cross_sum = [0,0]
    #print(len(num_list))
    
    for i in range(100):
        for j in range(100):
            row_sum[i] += num_list[i][j]
            col_sum[j] += num_list[i][j]
            if i == j : cross_sum[0] += num_list[i][j]
            if i == 99-j : cross_sum[1] += num_list[i][j]

    
    answer = max(max(row_sum), max(col_sum), max(cross_sum))
    print(f"#{test_case} {answer}")