'''
실버 3 문제
2와 5로 나누어 떨어지지 않는 정수 n이 주어졌을떄 각 자리수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램
이 말은 어떤 수 n이 주어지고 이는 2, 5로 나누어지지 않는 수이다. 이때 n의 배수중 각 자리수가 모두 1로 이루어진
예를 들어 111 이런식으로 이루어진 가장 작은 수를 찾은 후 이게 몇자리 수인지 출력하는 문제
여기서 모든 자리수가 1로 이루어진것을 어떻게 확인할 수 있는가?
-->10으로 나눠서 나머지 1, 100으로 나누어서 나머지 10, 1000으로 나누어서 나머지 100이런식으로 
나머지가 자기자신이 나오는 경우 나누기 중지하기
그 배수의 자리수를 어떻게 구할 것인가?
--> 앞에서 10의 n승 만큼으로 나누는 것을 활용하여 자리수를 구할 수 있을 것으로 판단된다.
'''

'''
첫번째 완성한 코드는 자리수에 1을 포함하는 지 밖에 구해지지 않음
-->
11로 나눈고 111로 나누면서 계속 나머지가 자기 자신이나 0이 나오는 지를 확인
자기 자신으로 나누었을 때 나머지가 0으로 나와야 한다.

두번쨰 완성한 코드는 1로 만 이루어져 있는지를 확인할 수 있다.
그러나 모든 n의 배수에 대해서 11을 늘려가며 확인하기에 시간이 너무 오래걸린다.
div 를 늘려가는 건 그렇게 큰 문제은 아니라고 생각된다
중요한 점은 모든 배수에 대해서 전부 확인하는 것이 시간이 너무 많이 든다는 것 --> 모든 배수를 확인하지 말아야 한다.
mul < div 일 때 k를 늘리는 방식에 변화를 주어야 할 듯? 11과 111 사이에는 갭이 있기에 전부 확인할 필요가 없다.

그렇다면 앞에서 작은 부분부터 111이 구해질 것이고 그 다음부터는 k를 10씩 증가시키면 될 것 같다.
끝에 1을 찾기 위해서는 10으로 나누었을때 1, 두번째 1을 찾기 위해서는 100으로 나누었을 때 11
'''

'''
정말 간단한 문제였다. 생각의 전환이 필요하다.
n의 배수가 111...을 만족하는 지를 직접 확인할 필요가 없이 111... 이 n으로 나누어 떨어지는지를 확인하면 되는 아주 간단한 문제이다.
'''


while(True): #테스트 케이스 별 반복문
    try:
        n = int(input())

        if n % 2 == 0 or n % 5 == 0:
            break
        
        check = 1
        multi = 1
        answer = 1
        while(True):
            if check % n == 0:
                break
            else:
                check = check + 10**multi #비교할 수를 1...씩 늘려감
                answer += 1
                multi += 1
        
        print(answer)
    except EOFError: #이 부분은 입력이 더이상 주어지지 않는 경우 종료하는 코드 --> 문제에서 종료 조건을 정확하게 주지 않음
        break