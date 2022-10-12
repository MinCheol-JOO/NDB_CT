## 경쟁적 전염

# NxN 크기의 시험관
# 바이러스의 종류 K개(1~K번)
# 1초마다 상하좌우 방향으로 증식, 번호가 낮은 종류의 바이러스부터 먼저 증식
# 낮은 번호부터 전염되는 조건을 확인해서 풀어나간다.(오름차순)

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n,k = map(int, input().split()) # N: 시험관 크기, K: 바이러스 종류 수
graph = []      # 시험관
virus_info = [] # 0이 아닌 바이러스에 대한 정보

# 시험관 정보

for i in range(n):
    graph.append(list(map(int, input().split())))
    # 간선 연결
    for j in range(n):
        if graph[i][j] != 0:
            virus_info.append((graph[i][j], i, j, 0))   # 바이러스 숫자, 위치(x,y), 시간(초)

virus_info.sort()       # 작은 숫자의 종류부터 증식시키기 위해 오름차순으로 정렬
queue = deque(virus_info)
s,x,y, = map(int, input().split())      # S: 초, X,Y: 각각 행과 열의 위치

### BFS ###

while queue:
    virus, a, b, time = queue.popleft()     # 바이러스 숫자, 위치(x,y), 시간(초) 뽑아내기

    if time == s:       # 알고자 하는 시간 s초가 되면 중지
        break

    for i in range(4):  # 상하좌우 탐색
        nx = a + dx[i]
        ny = b + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:      # 바이러스가 확산될 수 있는 위치라면
                graph[nx][ny] = virus   # 동일한 바이러스로 감염시킨다.
                queue.append((virus, nx, ny, time+1))   # 1초 증가시키고 다음으로 이동

print(graph[x-1][y-1])