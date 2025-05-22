T = int(input())

for test_case in range(1,T+1):
    size = int(input())
    grid = [[0]*size for _ in range(size)]
    has_num = [[False]*size for _ in range(size)]

    row = 0
    col = 0
    is_right = True
    is_left = False
    is_up = False
    is_down = False

    for number in range(1, size*size+1):
        grid[row][col] = number
        has_num[row][col] = True
        if is_right:
            if col != size-1 and has_num[row][col+1] == False:
                col += 1
            else:
                row += 1
                is_right = False
                is_down = True
        elif is_down:
            if row != size-1 and has_num[row+1][col] == False:
                row += 1
            else:
                col -= 1
                is_down = False
                is_left = True
        elif is_left:
            if col != 0 and has_num[row][col-1] == False:
                col -= 1
            else:
                row -= 1
                is_left = False
                is_up = True
        elif is_up:
            if row != 0 and has_num[row-1][col] == False:
                row -= 1
            else:
                col += 1
                is_up = False
                is_right = True
    
    print(f"#{test_case}")
    for i in range(size):
        for j in range(size):
            print(grid[i][j], end=" ")
        print()
    