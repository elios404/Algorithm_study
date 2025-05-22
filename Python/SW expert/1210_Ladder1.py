#뭔가 왜 틀렸는지 잘 모르겠음

def find_way(i):
    global grid
    find_exit = False

    for row in range(100):
        if i > 0 and grid[row][i-1] == 1:
            while i > 0 and grid[row][i-1] != 1:
                i -= 1
        elif i < 99 and grid[row][i+1] == 1:
            while i < 99 and grid[row][i+1] != 1:
                i += 1
        if row == 99 and grid[row][i] == 2:
            find_exit = True
    
    return find_exit

for _ in range(1):
    test_case = int(input())
    grid = []
    for _ in range(100):
        row = list(map(int, input().split()))
        grid.append(row)
    
    for col in range(100):
        if grid[0][col] == 1:
            if find_way(col):
                answer = col
                #break
        
    print(f"#{test_case} {answer}")