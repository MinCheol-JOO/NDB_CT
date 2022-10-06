from collections import deque

# 도시 개수 n, 도로 개수 m, 최단 거리 k, 출발 도시 x
n, m, k, x = map(int, input().split())

# 도시 간 연결 정보 초기화
city = [[] for _ in range(n+1)]
# 연결된 도시 정보 저장
for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)

# 거리 정보 초기화
distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시의 거리 = 0

# x 도시에서 출발
q = deque([x])
# 계속 도시가 연결되어 있는 한
while q:
    name = q.popleft() # 현재 출발 도시
    for c in city[name]: # 연결된 도시 탐색
        if distance[c] == -1: # 아직 탐색 전이면
            distance[c] = distance[name] + 1 # 거리 +1
            q.append(c) # 다녀갈 도시에 추가
            
if k in distance: # k 거리의 도시가 있다면
    for city_name, dist in enumerate(distance):
        if dist == k:
            print(city_name)
else: # k 거리의 도시가 없다면
    print(-1)