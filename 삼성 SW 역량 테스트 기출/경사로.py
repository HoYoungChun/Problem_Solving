def is_valid(i, installed, road, height):
  # !높이도 체크해야 함!
  # 범위안에 있고 경사로 설치 안되어 있을 때
  if 0<=i<N and road[i]==height and not installed[i]:
    return True
  return False
  

def check_one_road(road):
  installed = [False]*N # 경사로 설치 여부
  
  for ptr in range(N-1): # 하나씩 체크(왼쪽칸 기준으로 탐색)
    if road[ptr] == road[ptr+1]+1: #왼쪽이 한칸 더 큰 경우
      check_height = road[ptr+1]
      # 경사로 설치 가능한지 체크 => 불가능하면 False 바로 리턴
      for i in range(L):
        if not is_valid(ptr+1+i, installed, road, check_height): #ptr+1부터
          return False
          
      # 경사로 설치(installed=True로)
      for i in range(L):
        installed[ptr+1+i] = True
      
    elif road[ptr]+1 == road[ptr+1]: # 오른쪽이 한칸 더 큰 경우
      check_height = road[ptr]
      # 경사로 설치 가능한지 체크 => 불가능하면 False 바로 리턴
      for i in range(L):
        if not is_valid(ptr-i, installed, road, check_height):# ptr부터
          return False

      # 경사로 설치(installed=True로)
      for i in range(L):
        installed[ptr-i] = True
      
    elif road[ptr]==road[ptr+1]: # 높이 같은 경우
      continue # 다음 칸으로 이동
    else: # 2칸 이상 차이 나는 경우 바로 False 반환
      return False
      
  return True


N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

ans = 0
# 가로 방향
for i in range(N):
  road = []
  for j in range(N):
    road.append(graph[i][j])
  if check_one_road(road):
    ans +=1

# 세로 방향
for i in range(N):
  road = []
  for j in range(N):
    road.append(graph[j][i])
  if check_one_road(road):
    ans +=1

print(ans)
