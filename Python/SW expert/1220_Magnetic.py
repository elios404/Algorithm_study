#T = int(input())

for test_case in range(1, 11):
    grid_size = int(input())
    grid = []
    for i in range(grid_size):
        row = list(map(int, input().split()))
        grid.append(row)
    
    answer = 0
    check = False
    for c in range(grid_size):
        for r in range(grid_size):
            if not check and grid[r][c] == 1:
                check = True
            elif check and grid[r][c] == 2:
                check = False
                answer += 1
        check = False
    
    print(f"#{test_case} {answer}")