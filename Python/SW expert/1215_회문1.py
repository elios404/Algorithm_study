#같은 회문이라도 여러 번 등장하면 계속 카운트 하는 것인가? --> 같은 회문이라도 여러 번 체크
#문자열이 주어졌을 때 회문인지 어떻게 확인할 것인가?

for T in range(1):
    answer = 0
    n = int(input())
    grid = []
    for i in range(8):
        r = input()
        row = [c for c in r]
        grid.append(row)
    
    round_set = set()

    #row
    for i in range(8):
        for j in range(9-n):
            line = grid[i][j:j+n]
            is_round = True
            check = 0
            while(is_round):
                if check > n-1-check: #회문임이 확인 되었을 때
                    break
                elif line[check] != line[n-1-check]: #회문이 아니라면
                    is_round = False
                else:
                    check += 1
            if is_round:
                round_set.add(tuple(line))
                answer += 1
    
    #col
    for i in range(9-n):
        for j in range(8):
            line = [grid[idx][j] for idx in range(i,i+n)]
            is_round = True
            check = 0
            while(is_round):
                if check > n-1-check: #회문임이 확인 되었을 때
                    break
                elif line[check] != line[n-1-check]: #회문이 아니라면
                    is_round = False
                else:
                    check += 1
            if is_round:
                round_set.add(tuple(line))
                answer += 1
    
    print(f"#{T+1} {answer}")