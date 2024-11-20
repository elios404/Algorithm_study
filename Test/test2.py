test_num = int(input())

for T in range(test_num):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ksum_list = [0]*(n-k+1)

    for i in range(n-k+1):
        sub_list = arr[i:i+k]
        ksum_list[i] = sum(sub_list)
    #print(ksum_list)
    max1 = float('-inf')
    max1_idx = -1
    max2 = float('-inf')
    max2_idx  = -1
    for i in range(len(ksum_list)):
        if ksum_list[i] > max1:
            max1 = ksum_list[i]
            max1_idx = i
    #print(max1, max1_idx)
    sec_ksum_list = ksum_list[0:max1_idx-k+1] + ksum_list[max1_idx + k:]
    #print(sec_ksum_list)
    for i in range(len(sec_ksum_list)):
        if sec_ksum_list[i] > max2:
            max2 = sec_ksum_list[i]
            max2_idx = i
    #print(max2, max2_idx)

    print(f"#{T+1} {max1+max2}")
