# ! x,y 좌표 평소 풀던 방향과 반대임
DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 오른쪽, 위, 왼쪽, 아래


def get_dir_idxs(start_dir_idx, generation):
    dir_idxs = [start_dir_idx]
    for _ in range(generation):
        dir_idxs += list(map(lambda x: (x + 1) % 4, dir_idxs[::-1]))  # 뒤집어서
    return dir_idxs


visited = [[False] * 101 for _ in range(101)]  # 커브 놓이면 True로(점 기준)
N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    visited[x][y] = True
    dir_idxs = get_dir_idxs(d, g)
    for dir_idx in dir_idxs:
        dx, dy = DIRECTIONS[dir_idx]
        x, y = x + dx, y + dy
        visited[x][y] = True

ans = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i + 1][j] \
        and visited[i][j + 1] and visited[i + 1][j + 1]:
            ans += 1

print(ans)
