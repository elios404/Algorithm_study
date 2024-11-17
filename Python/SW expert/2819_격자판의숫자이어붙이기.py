#조건을 보면 시간이 짧다. 아마 해시로 시간을 절약해야 할 듯 하다.
#어느 숫자 옆에 다른 숫자가 있는지 확인하고 저장한다면?

test_num = int(input())

for T in range(test_num):
    arr = []
    for i in range(4):
        l = list(input().split())
        arr.append(l)
    
    near_dict = {}
    dy = [-1,0,1,0]; dx = [0,-1,0,1]
    for i in range(4):
        for j in range(4):
            val = arr[i][j]
            for k in range(4):
                ny, nx = i+dy[k], j+dx[k]
                if 0 <= ny < 4 and 0 <= nx < 4:
                    near_val = arr[ny][nx]
                    if val not in near_dict : near_dict[val] = set(near_val)
                    else : near_dict[val].add(near_val)
    
    keys = near_dict.keys()
    for i in range(6):
        next_keys = set()
        for key in keys:
            last_s = key[-1]
            can_come = near_dict[last_s] #set
            for come in can_come:
                next_key = key+come
                next_keys.add(next_key)
        keys = next_keys
        print(keys)
    
    print(f"#{T+1} {len(keys)}")