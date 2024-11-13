#스타트와 링크 문제
from itertools import combinations

n = int(input())
member = [i for i in range(n)]
grid = []
for i in range(n):
    g = list(map(int, input().split()))
    grid.append(g)

gap = 10*6
start_list = list(combinations(member, int(n/2)))

for start in start_list:
    link = [m for m in member if m not in start]
    start_score = 0
    for i in start:
        for j in start:
            start_score += grid[i][j]
    link_score = 0
    for i in link:
        for j in link:
            link_score += grid[i][j]
    
    gap = min(gap, abs(start_score - link_score))

print(gap)