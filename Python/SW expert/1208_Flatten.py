for test_case in range(1,11):
    dump_count = int(input())
    boxs = list(map(int,input().split()))
    boxs.sort(reverse=True)
    #print(boxs)

    for dump in range(dump_count):
        max_height_idx = next((idx for idx in range(len(boxs)) if  boxs[idx] > boxs[idx+1]), None)
        min_height_idx = next((idx for idx in range(len(boxs)-1, 0, -1) if boxs[idx] < boxs[idx-1]), None)
        boxs[max_height_idx] -= 1
        boxs[min_height_idx] += 1
        #print(boxs)

    answer = boxs[0] - boxs[-1]
    print(f"#{test_case} {answer}")