
def cal_connection(grid, core_count, connected_core, connected_length):
    global max_core, min_length, where_core, N
    if core_count == core_num:
        if max_core < connected_core:
            max_core = connected_core
            min_length = connected_length
        elif max_core == connected_core:
            min_length = min(min_length, connected_length)
        return
    
    core_loc = where_core[core_count]
    core_y, core_x = core_loc[0], core_loc[1]
    if core_y == 0 or core_y == N or core_x == 0 or core_x == N: #외각에 있는 코어라면
        cal_connection(grid, core_count+1, connected_core+1, connected_length)
    else:
        #위쪽 확인 
        is_top_check = True
        top_check = [(core_y-i, core_x) for i in range(1,core_y+1)]
        for check in top_check:
            if grid[check[0]][check[1]] == 1 or grid[check[0]][check[1]] == 2:
                is_top_check = False
                break
        if is_top_check:
            for check in top_check:
                grid[check[0]][check[1]] = 2
            cal_connection(grid,core_count+1, connected_core+1, connected_length+len(top_check))
            for check in top_check:
                grid[check[0]][check[1]] = 0
        
        #오른쪽 확인
        is_right_check = True
        right_check = [(core_y, core_x+i) for i in range(1,N-core_x)]
        for check in right_check:
            if grid[check[0]][check[1]] == 1 or grid[check[0]][check[1]] == 2:
                is_right_check = False
                break
        if is_right_check:
            for check in right_check:
                grid[check[0]][check[1]] = 2
            cal_connection(grid,core_count+1, connected_core+1, connected_length+len(right_check))
            for check in right_check:
                grid[check[0]][check[1]] = 0

        #아래쪽 확인
        is_down_check = True
        down_check = [(core_y+i, core_x) for i in range(1,N-core_y)]
        for check in down_check:
            if grid[check[0]][check[1]] == 1 or grid[check[0]][check[1]] == 2:
                is_down_check = False
                break
        if is_down_check:
            for check in down_check:
                grid[check[0]][check[1]] = 2
            cal_connection(grid,core_count+1, connected_core+1, connected_length+len(down_check))
            for check in down_check:
                grid[check[0]][check[1]] = 0

        #왼쪽 확인
        is_left_check = True
        left_check = [(core_y, core_x-i) for i in range(1,core_x+1)]
        for check in left_check:
            if grid[check[0]][check[1]] == 1 or grid[check[0]][check[1]] == 2:
                is_left_check = False
                break
        if is_left_check:
            for check in left_check:
                grid[check[0]][check[1]] = 2
            cal_connection(grid,core_count+1, connected_core+1, connected_length+len(left_check))
            for check in left_check:
                grid[check[0]][check[1]] = 0
        
        #아무곳도 가지 않음
        cal_connection(grid, core_count+1, connected_core, connected_length)
    

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    grid = []

    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)

    where_core = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                where_core.append((i,j))
    
    core_num = len(where_core)
    max_core = 0
    min_length = float('inf')

    cal_connection(grid, 0,0,0)

    print(f"#{test_case} {min_length}")
