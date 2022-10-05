n,m = map(int,input().split())
graph = []
for _ in range(n):
    b = list(map(int,input().split()))
    graph.append(b)


def dfs(x,y):
    if x>m-1 or x<0 or y>n-1 or y<0 or graph[x][y]==1:
        return
    
    if graph[x][y] ==0:
        graph[x][y]=2
            
    if graph[x][y] ==2 or graph[x][y]==0:
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
        
        
dfs(0,0)
cnt = 0
for i in graph:
    cnt+=i.count(1)
print(cnt)