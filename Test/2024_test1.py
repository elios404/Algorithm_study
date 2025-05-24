from collections import deque
test_num = int(input())

for T in range(test_num):
    n, k = map(int, input().split())
    arr = deque(list(map(int, input().split())))

    turn = 0
    arr_turn = []
    while(True):
        if turn > n:
            if turn%(n-1) == 0:
                if arr_turn == list(arr): #반복해도 달라지지 않는다면
                    turn = -1
                    break
                else :
                    arr_turn = [a for a in arr]

        Finish = True
        check_num = arr[0]
        for i in range(n):
            #print(f"first {check_num} arr[i] {arr[i]}")
            if check_num != arr[i]:
                Finish = False
                break
        
        if Finish:
            break
        else:
            k_num = arr[k-1]
            arr.popleft()
            arr.append(k_num)
            turn += 1

    print(f"#{T+1} {turn}")
