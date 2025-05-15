#파이썬에서 set을 함수의 매개변수로 넣어줄 경우 참조형식으로 들어간다. 재귀함수로 들어가면 계속 같은 set을 공유한다.
#따라서 이 경우 재귀함수로 들어간 노드를 다시 제거해 주어서 초기 상태로 되돌려야 한다.

def find_route(start_node, visited):
    global connect, n, answer
    visited.add(start_node)

    no_way = True
    for i in range(n):
        if i not in visited and connect[start_node][i] == True:
            no_way = False
            find_route(i,visited)
            visited.remove(i)
    if no_way:
        answer = max(answer, len(visited))
        return

T = int(input())

for test_case in range(1,T+1):
    n, m = map(int, input().split())
    connect = [[False]*n for _ in range(n)]
    answer = 0
    #row = start node, col = end node
    
    for _ in range(m):
        node1, node2 = map(int, input().split())
        node1 -= 1
        node2 -= 1
        connect[node1][node2] = True
        connect[node2][node1] = True
    
    for i in range(n):
        visited = set()
        find_route(i,visited)

    print(f"#{test_case} {answer}")