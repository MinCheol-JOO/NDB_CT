from itertools import combinations

n, m = map(int, input().split()) # 도시 크기 n * n, 선택한 치킨집 갯수 m

house, chicken = [], [] 
for x in range(n):
    a = list(map(int, input().split()))
    for y in range(n):
        if a[y] == 1:
            house.append((x, y))
        elif a[y] == 2:
            chicken.append((x, y))
            
chicken_list = list(combinations(chicken, m)) # m개의 치킨집 조합 list

answer = 1e9 # m개 치킨집을 골랐을 때 치킨거리: 가장 짧은 거리를 구해야하니까
for chick in chicken_list: # 치킨집 조합 list에서 하나씩 꺼내면서
    dist_total = 0 # 총 치킨거리 초기화
    for h_x, h_y in house: # 각각의 집에 대하여
        dist_one = 1e9 # 치킨집 하나에 대한 치킨거리: 가장 짧은 거리를 구해야하니까
        for c_x, c_y in chick: # 각각의 치킨집에 대하여
            # 해당 치킨집에 대한 치킨거리 구하기
            dist_one = min(dist_one, abs(h_x - c_x) + abs(h_y - c_y))
        dist_total += dist_one # 해당 집의 총 치킨거리 구하기
    answer = min(answer, dist_total) # 전체 가장 짧은 치킨거리 구하기
    print(answer)
print(answer)