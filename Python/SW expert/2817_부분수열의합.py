def search(idx, sum):
    global nums, answer, n, k
    if idx == n:
        return
    new_sum = sum + nums[idx]
    if new_sum > k:
        search(idx+1, sum)
    elif new_sum == k:
        answer += 1
        search(idx+1, sum)
    else:
        search(idx+1, new_sum)
        search(idx+1, sum)

T = int(input())

for test_case in range(1,T+1):
    n,k = map(int,input().split())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    answer = 0
    
    search(0,0)

    print(f"#{test_case} {answer}")
        