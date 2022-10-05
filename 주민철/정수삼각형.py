# n = int(input())
# array = []
# for i in range(n):
#     a = list(map(int,input().split()))
#     array.append(a)

# d = [0 for _ in range(500+1)]
# d[1] = array[0][0]
# for i in range(1,n): # row의 갯수
#     for j in range(i+1): # column의 갯수
#         if j-1<0:
#             left = 0
#         else:
#             left = array[i-1][j-1]
#         if j+1>i:
#             right = 0
#         else:
#             right = array[i-1][j]

#         array[i][j] = array[i][j]+ max(left,right)

# print(max(array[n-1])) 
n= int(input())
graph = []
for _ in range(n):
    a = list(map(int,input().split()))
    graph.append(a)

start = 0
sum =0
# sum+=graph[0][0]
start_y = 0
for i in range(1,n): # row 개수만큼 내려와야겠지
    for j in range(i+1): # column이 0이면
        if j == 0:
            # 그대로 내려온다
            up_left = 0
        else:
            # 리스트는 크기만이 올라갈뿐
            up_left = graph[i-1][j-1]
            
        if i==j:
            up = 0
        else:
            up = graph[i-1][j]
            
        graph[i][j]+=max(up,up_left)
        
print(graph)