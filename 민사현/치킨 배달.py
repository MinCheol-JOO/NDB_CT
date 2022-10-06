#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 13. 치킨 배달

from itertools import combinations

# 집, 치킨집 좌표
n, m = map(int,input().split())
house, chicken = [], []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: # 1:house
            house.append((i,j))
        elif data[j] == 2: # 2:chicken
            chicken.append((i,j))
            
# m개 치킨집만 영업
winner = list(combinations(chicken, m))

# 치킨거리
def chicken_dis(winner):
    result = 0
    for hx, hy in house:
        tmp = float('inf')
        for cx, xy in chicken:
            tmp = min(tmp, abs(hx-cx) + abs(hy-cy))
        result += tmp
    return result

result = float('inf')
for w in winner:
    result = min(result, chicken_dis(w))
    
print(result)

