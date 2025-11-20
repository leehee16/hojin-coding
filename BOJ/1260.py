from collections import deque

if __name__ == "__main__":
    n,m,v = map(int,input().split())
    graph = [[0]*(n+1) for _ in range(n+1)] 
    for _ in range(m):
        x,y = map(int,input().split())
        graph[x][y] = 1
        graph[y][x] = 1
    
    visited = [False]*(n+1)

    def dfs(idx):
        visited[idx] = True
        print(idx, end=' ')
        for nxt in range(1, n+1):
            if graph[idx][nxt] == 1 and not visited[nxt]:
                dfs(nxt)
    


    def bfs(start):
        q = deque()
        q.append(start)
        visited[start] = True
        print(start, end=' ')
        
        while q:
            x = q.popleft()
            for nxt in range(1, n+1):
                if graph[x][nxt] == 1 and not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
                    print(nxt, end=' ')
    dfs(v)
    print()  # 줄바꿈
    
    visited = [False] * (n + 1)  # 방문 초기화
    bfs(v)