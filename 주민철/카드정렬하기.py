n = int(input())
heap = []
import heapq
for _ in range(n):
    heapq.heappush(heap,int(input()))
    
import heapq
sum = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # print([one,two])
    three = one+two
    
    # print(three)
    sum+=three
    heapq.heappush(heap,three)

# print(heap)
# print(heapq.heappop(heap))
print(sum)
