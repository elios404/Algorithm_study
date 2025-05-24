#문제이름 : 광고
# n 명의 사용자가 있다. 각 사용자는 광고의 수가 몇 개 이하인 경우 무료로 보고 이때 광고 당 B의 수익을 얻는다.
# n 명의 사용자 별 사용자의 한계 광고수를 넘기면 사용자는 유료서비스로 전환하고 광고 수에 상관없이 P의 수익을 얻는다.
# 회사가 얻을 수 있는 최대 수익을 구하라. 다른말로 몇 개의 광고를 보여줘야 최대 수익을 얻을 수 있는가

T = int(input())

for test_case in range(1, T+1):
    N,P,B = map(int,input().split())
    free_ad = list(map(int,input().split()))
    most_ad = max(free_ad)
    most_money = 0

    #광고의 수가 1개부터 점점 늘어나야 한다.
    for ad in range(most_ad+2):
        can_earn = 0
        for person_ad in free_ad:
            if ad <= person_ad:
                can_earn += B*ad
            else:
                can_earn += P
        
        if can_earn > most_money:
            most_money = can_earn
    
    print(f"#{test_case} {most_money}")