## 14502
## 연구소 - dfs

import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0

# 바이러스 확산
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if wall[nx][ny] == 0:
                wall[nx][ny]=2  # 바이러스 배치
                virus(nx,ny)    # 재귀 수행
    return  

def dfs(cnt):
    global ans

    # 벽은 꼭 3개를 세워야 함. 세운 벽 결과에 반영하고 안전영역 계산
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                wall[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                # 바이러스 확산
                if wall[i][j] == 2:
                    virus(i,j)

        # 벽 설치, 바이러스 확산 후 안전영역 계산
        score = 0
        for i in range(n):
            for j in range(m):
                if wall[i][j] == 0:
                    score += 1
 
        ans = max(ans, score)
        return


    # 벽 세우기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                dfs(cnt)
            else:
                graph[i][j] = 0
                cnt -= 1

### main ###

n,m = map(int, input().rstrip().split())

graph = []      # 맨 처음
wall = [[0]*m for _i in range(n)]       # 벽 설치 후

for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

dfs(0)

# 안전영역의 최댓값
print(ans)