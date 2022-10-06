# 실패인데, 리뷰 받고자 올립니다 ㅠㅠ 성공하면 바로 수정하는걸루..

from itertools import combinations

# 2. 바이러스가 퍼짐
def virus(space):
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동서남북 방향
    for d_x, d_y in dir:
        next_x, next_y = x + d_x, y + d_y
        if (0 <= next_x < n) and (0 <= next_y < m):
            space[next_x][next_y] = 2
            virus(space, x, y)
    
# 3. 안전지대 count
def safe(space):
    result = 0
    for s in space:
        result += s.count(0)
    return result

# 이제, 실행해보자
n, m = map(int, input().split())

labs, labs_zero = [], []
result = 0
for x in range(n):
    lab = list(map(int, input().split()))
    labs.append(lab) # 연구소 정보
    
    for y in range(m):
        if not lab[y]:
            labs_zero.append((x, y)) # 연구소 빈칸 정보
            
# 연구소 list 복사: 2차원 list 복사(깊은복사)
## deepcopy를 사용해도 되지만, 엄청 느림
labs_copy = [lab[:] for lab in labs]

# 1. 벽 3개 세우기: combination으로 경우의 수 구하기
for wall in list(combinations(labs_zero, 3)):
    for w_x, w_y in wall:
        labs_copy[w_x][w_y] = 1
    # 2. 파이러스가 퍼짐
    virus(labs_copy)
    # 3. 안전지대 count
    result = max(result, safe(labs_copy))

print(result)