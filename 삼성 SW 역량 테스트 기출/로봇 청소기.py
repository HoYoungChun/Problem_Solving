EMPTY, WALL = 0, 1
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

find_left = [(0,-1),(-1,0),(0,1),(1,0)] # 방향 d 인덱스 기준으로 왼쪽 방향 찾기
find_back = [(1,0),(0,-1),(-1,0),(0,1)] # 방향 d 인덱스 기준으로 뒤 방향 찾기

def is_valid(r,c):
  if 0<=r<N and 0<=c<M and room[r][c] == EMPTY and not cleaned[r][c]:
    return True
  return False

N, M = map(int,input().split())
cleaned = [[False]*M for _ in range(N)] # 청소된 곳은 True로 변경

r,c,d = map(int,input().split())
room = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
  if not cleaned[r][c]: # 1. 현재 위치를 청소한다.
    cleaned[r][c]=True
    ans +=1

  # 2-3. 네 방향 모두 청소되어있거나 벽이면 한칸 후진, 2번으로
  can_move = False
  for dx, dy in find_left:
    if is_valid(r+dx,c+dy):
      can_move = True
      
  if not can_move: # 움직일 곳 없을 때
    dx, dy = find_back[d]
    # 후진 불가능 2-4. 뒤쪽 방향이 벽이라 후진 안되면 작동 멈춘다.
    if room[r+dx][c+dy]==WALL:
      break
    else: # 후진 가능
      r,c = r+dx, c+dy
      continue

  #2. 왼쪽 방향부터 탐색
  dx,dy = find_left[d]
  
  #2-1. 왼쪽 방향에 청소하지 않은 공간이 존재한다면
  if is_valid(r+dx, c+dy):
    d = (d+3)%4 # 회전
    r,c = r+dx, c+dy # 전진
    continue

  #2-2. 회전만
  else:
    d = (d+3)%4 # 회전

print(ans)