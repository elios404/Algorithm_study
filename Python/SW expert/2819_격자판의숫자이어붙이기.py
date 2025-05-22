def make_number(row, col, seq, number):
    global grid, number_can_make
    number = number*10 + grid[row][col]
    if seq == 7:
        number_can_make.add(number)
        return
    move_y = [0,1,0,-1] #세로이동 row 이동
    move_x = [1,0,-1,0] #가로이동 col 이동

    for i in range(4):
        new_row = row+move_y[i]
        new_col = col+move_x[i]
        if new_row >= 0 and new_row < 4 and new_col >= 0 and new_col < 4:
            make_number(new_row, new_col, seq+1,number)


T = int(input())

for test_case in range(1,T+1):
    grid = []
    for _ in range(4):
        row = list(map(int,input().split()))
        grid.append(row)
    
    number_can_make = set()

    for i in range(4):
        for j in range(4):
            make_number(i,j,1,0)
    
    #print(number_can_make)
    print(f"#{test_case} {len(number_can_make)}")