DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def is_valid(x, y):
    # 범위안에 있고 공기청정기 없는 곳 일때
    if 0 <= x < R and 0 <= y < C and (x, y) not in [(up_x, 0), (down_x, 0)]:
        return True
    return False


def diffusion():
    # 미세먼지 확산하는 함수
    diffused_graph = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:  # 미세먼지 존재
                now_dust = graph[i][j]
                diffuse_dust = now_dust // 5
                for dx, dy in DIRECTIONS:
                    if is_valid(i + dx, j + dy):  # 공기청정기나 벽 아닐때
                        diffused_graph[i + dx][j + dy] += diffuse_dust
                        now_dust -= diffuse_dust
                diffused_graph[i][j] += now_dust

    return diffused_graph


def move(start_x, dx_dy):
    x, y = start_x, 0
    for dx, dy in dx_dy:  # (x,y) 에 (x+dx, y+dy)를 옮김
        if (x, y) not in [(up_x, 0), (down_x, 0)]:  # 공기청정기 있는 곳은 땡기면 안됨
            graph[x][y] = graph[x + dx][y + dy]
        graph[x + dx][y + dy] = 0
        x, y = x + dx, y + dy


R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if graph[i][0] == -1:
        up_x = i
        down_x = i + 1
        graph[up_x][0] = 0  # 이후에 공기청정기 있는 곳은 항상 0으로
        graph[down_x][0] = 0
        break

for _ in range(T):
    # 1. 미세먼지 확산
    graph = diffusion()

    # 2. 공기청정기 작동
    up_dx_dy = [(-1, 0)] * up_x + [(0, 1)] * (C - 1) + [(1, 0)] * up_x + [
        (0, -1)
    ] * (C - 1)
    move(up_x, up_dx_dy)

    down_dx_dy = [(1, 0)] * (R - 1 - down_x) + [(0, 1)] * (C - 1) + [
        (-1, 0)
    ] * (R - 1 - down_x) + [(0, -1)] * (C - 1)
    move(down_x, down_dx_dy)

print(sum(sum(l) for l in graph))
