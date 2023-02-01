import sys
input=sys.stdin.readline

def is_valid(x,y):
  if 0<=x<N and 0<=y<M and not visited[x][y]:
    return True
  return False

def is_valid_diag(x,y): # 이동할 곳 x,y기준 붙어있는 곳 하나 있어야 됨
  if 0<=x<N and 0<=y<M and not visited[x][y]:
      for dx, dy in direction:
        if 0<=x+dx<N and 0<=y+dy<M and visited[x+dx][y+dy]:
          return True
  return False

def dfs(x,y,cnt,cum_sum):
  global max_sum # 값의 변경이 필요하므로
  
  if cnt == 4:
    max_sum = max(max_sum, cum_sum)
    return

  for dx, dy in direction: # 수평, 수직 이동
    new_x,new_y = x+dx, y+dy
    if is_valid(new_x, new_y):
      visited[new_x][new_y]=True # 다른 DFS의 visited에도 영향을 미친다
      dfs(new_x, new_y, cnt+1, cum_sum+paper[new_x][new_y])
      visited[new_x][new_y]=False # 다시 False로 둬야 다른 DFS에 영향 안미친다

  for dx, dy in diagonal: # 대각선 이동
    new_x, new_y = x+dx, y+dy
    if is_valid_diag(new_x,new_y):
      visited[new_x][new_y]=True
      dfs(new_x, new_y, cnt+1, cum_sum+paper[new_x][new_y])
      visited[new_x][new_y]=False

direction = [(0,1),(1,0),(0,-1),(-1,0)] # 수직, 수평 방향
diagonal = [(1,1),(-1,-1),(1,-1),(-1,1)] # 대각선 방향
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

max_sum = -float('inf')
visited = [[False]*M for _ in range(N)] # 방문여부 초기화 1번만
for i in range(N):
  for j in range(M):
    visited[i][j] = True
    dfs(i,j,1,paper[i][j])
    visited[i][j] = False # 매번 초기화하는대신 여기서 다시 원복
print(max_sum)
