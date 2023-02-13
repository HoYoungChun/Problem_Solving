from collections import deque

DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 위, 왼쪽, 오른쪽, 아래


class BabyFish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 2  # 초기 사이즈
        self.eat_num = 0  # 크기 갱신될때마다 초기화

    def size_up(self):  # 물고기 먹었을때
        self.eat_num += 1
        if self.size == self.eat_num:
            self.size += 1
            self.eat_num = 0


# def eat_avaliable():  # 먹을 수 있는게 존재하는지
#     # !먹을 수 있어도 접근 못할 수 있다.
#     for i in range(N):
#         for j in range(N):
#             if graph[i][j] != 0 and graph[i][j] < baby_fish.size:
#                 return True
#     return False


def is_valid(x, y, visited):  # 이동할 수 있는지(0 or 같은 사이즈)
    if 0 <= x < N and 0 <= y < N and not visited[x][y] \
      and graph[x][y] <= baby_fish.size:
        return True
    return False


def bfs():
    eat_fish_list = []
    visited = [[False] * N for _ in range(N)]
    x, y = baby_fish.x, baby_fish.y

    visited[x][y] = True
    queue = deque([(x, y, 0)])  # (x,y,이동거리)
    while queue:
        x, y, distance = queue.popleft()
        if graph[x][y] != 0 and graph[x][y] < baby_fish.size:  # 먹을 수 있으면
            eat_fish_list.append((x, y, distance))

        for dx, dy in DIRECTIONS:
            if is_valid(x + dx, y + dy, visited):  # 0이나 작은 물고기
                visited[x + dx][y + dy] = True
                queue.append((x + dx, y + dy, distance + 1))

    if eat_fish_list:
        eat_fish_list.sort(key=lambda x:
                           (x[2], x[0], x[1]))  # 거리 짧, x좌표 작, y좌표 작
        return eat_fish_list[0]
    else:
        return -1, -1, -1  # 먹을게 없을때


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            baby_fish = BabyFish(i, j)  # 아기 상어 초기화
            graph[i][j] = 0  # 아기 상어 있던 곳을 빈 칸으로

ans = 0  # 몇 초 걸리는지
while True:
    eat_fish_x, eat_fish_y, distance = bfs()  # 먹을 물고기 x,y좌표랑 이동거리
    if distance == -1:  # 먹을게 없을때
        break

    ans += distance  # 정답 갱신
    baby_fish.x, baby_fish.y = eat_fish_x, eat_fish_y  # 아기상어 위치 갱신
    # 사이즈 갱신
    baby_fish.size_up()
    # 먹은 곳 0으로
    graph[eat_fish_x][eat_fish_y] = 0

print(ans)
