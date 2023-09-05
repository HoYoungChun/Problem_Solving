from collections import defaultdict

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]


def find_gap(nx, ny, d1, d2):
  """가장 큰 선거구 인원과 가장 선거구인원 차이의 최소값 반환"""
  pop_dict = defaultdict(int)

  for nr in range(N):
    for nc in range(N):
      if 0 <= nr < nx + d1 and 0 <= nc <= ny and (nr+nc)<(nx+ny):
        area_num = 1
      elif 0 <= nr <= nx + d2 and ny < nc <= N - 1 and (N-1-nc+nr)<(N-1-(ny+d2)+nx+d2):
        area_num = 2
      elif nx + d1 <= nr <= N - 1 and 0 <= nc < ny - d1 + d2 and (N-1-nr+nc)<(N-1-(nx+d1)+ny-d1):
        area_num = 3
      elif nx + d2 < nr <= N - 1 and ny - d1 + d2 <= nc <= N - 1 and (nr+nc)>(nx+ny+2*d2):
        area_num = 4
      else:
        area_num = 5

      #print(nr, nc, area_num)
      pop_dict[area_num] += maps[nr][nc]

  if len(pop_dict.keys()) != 5:
    return float('inf')

  return max(pop_dict.values()) - min(pop_dict.values())


res = float('inf')

# 인덱스 0부터로 생각(nx,ny), x,y는 인덱스1부터 기준
for nx in range(1, N-1):
  for ny in range(1, N-1):
    for d1 in range(1, ny+1): # 1 ~ ny
      for d2 in range(1, N-ny): # 1 ~ N-1-ny
        res = min(res,find_gap(nx,ny,d1,d2))

print(res)