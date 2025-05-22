days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

T = int(input())
for test_case in range(1, T+1):
    month1, day1, month2, day2 = map(int,input().split())
    result1 = day1
    for i in range(month1-1):
        result1 += days_in_month[i]
    result2 = day2
    for i in range(month2-1):
        result2 += days_in_month[i]
    print(f"#{test_case} {result2-result1+1}")