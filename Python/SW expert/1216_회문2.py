for _ in range(10):
    test_case = int(input())
    grid = []
    answer = 1

    for i in range(100):
        grid.append(list(input()))

    
    for r in range(100): #가로에 대해서
        row = grid[r]
        for count in range(100,1,-1):
            is_end = False
            for c in range(101-count):
                check_row = row[c:c+count] #c 가 시작 idx c+count 가 마지막 idx
                if check_row == check_row[::-1]:
                    answer = max(answer,count)
                    is_end = True
                    break
            if is_end:
                break

    for c in range(100):
        col = [row[c] for row in grid]
        for count in range(100, 1, -1):
            is_end = False
            for r in range(101-count):
                check_col = col[r:r+count]
                if check_col == check_col[::-1]:
                    answer = max(answer,count)
                    is_end = True
                    break
            if is_end:
                break

    print(f"#{test_case} {answer}")
                