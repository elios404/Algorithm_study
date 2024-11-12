test_num = int(input())

for T in range(test_num):
    n,m = map(int, input().split())
    grid = []
    for i in range(n):
        row = input()
        row_int = [int(c) for c in row]
        grid.append(row_int)
    
    idx = next(([r, c] for r in range(n) for c in range(m-1,-1,-1) if grid[r][c] == 1),None)
    code = grid[idx[0]][idx[1]-55:idx[1]+1]
    code_num = [0] * 8
    password = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, 
                '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

    for i in range(8):
        num_list = code[i*7:i*7+7]
        num = ''.join(map(str,num_list))
        code_num[i] = password[num]
    
    check = (code_num[0]+code_num[2]+code_num[4]+code_num[6])*3 +(code_num[1]+code_num[3]+code_num[5]+code_num[7])
    if check%10 == 0:
        print(f"#{T+1} {sum(code_num)}")
    else:
        print(f"#{T+1} 0")
