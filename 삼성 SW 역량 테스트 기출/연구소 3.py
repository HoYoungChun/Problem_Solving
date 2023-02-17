import sys
from itertools import combinations
from collections import deque

EMPTY, WALL, INACTIVE_VIRUS, ACTIVE_VIRUS = 0, 1, 2, 3
DX_DY = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상하좌우

input = sys.stdin.readline


def is_valid(x, y, graph, visited):
    """확산 대상인지 체크"""
    if 0 <= x < N and 0 <= y < N \
      and graph[x][y] in [EMPTY, INACTIVE_VIRUS] \
      and not visited[x][y]:
        return True
    return False


def bfs(graph, active_viruses, visited):
    queue = deque([])

    for x, y in active_viruses:
        visited[x][y] = True
        queue.append((x, y, 0))

    total_sec = 0
    while queue:
        x, y, sec = queue.popleft()

        if graph[x][y] == EMPTY: # 비활성-> 활성은 갱신X
          total_sec = max(total_sec, sec)
      
        for dx, dy in DX_DY:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, graph, visited):
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, sec + 1))
              
    return total_sec


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

all_virus_xy = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == INACTIVE_VIRUS:
            all_virus_xy.append((i, j))

ans = float('inf')
virus_combinations = map(list, combinations(all_virus_xy, M))
for active_viruses in virus_combinations:
    copied_graph = [l[:] for l in graph]  # 원복 복제
    for x, y in active_viruses:
        copied_graph[x][y] = ACTIVE_VIRUS  # 활성화된 곳 표시

    visited = [[False] * N for _ in range(N)]  # 방문한곳체크
    total_sec = bfs(copied_graph, active_viruses, visited) # 확산할수있는만큼한 시간

    impossible = False
    for i in range(N):
      for j in range(N):
        if is_valid(i,j,copied_graph, visited): # 확산되어야 하는데 안된 곳 있으면
          impossible = True
          
    if not impossible:
      ans = min(ans, total_sec)
      
          
# ans가 float('inf')면 -1 프린트 아니면 ans 출력
if ans == float('inf'):
    print(-1)
else:
    print(ans)
