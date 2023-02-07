from collections import OrderedDict  # 버전 이슈 없애기 위해
from itertools import product
from copy import deepcopy

UP, DOWN, LEFT, RIGHT = "UP", "DOWN", "LEFT", "RIGHT"
DX_DY = {UP: (-1, 0), DOWN: (1, 0), LEFT: (0, -1), RIGHT: (0, 1)}
WATCHABLE = "X"

CCTV_DIR_CANDIDATES = [
    None,
    [(UP, ), (DOWN, ), (LEFT, ), (RIGHT, )],  # 1번 CCTV
    [(UP, DOWN), (LEFT, RIGHT)],  # 2번 CCTV
    [(UP, RIGHT), (RIGHT, DOWN), (DOWN, LEFT), (LEFT, UP)],  # 3번 CCTV
    [(UP, DOWN, LEFT), (UP, DOWN, RIGHT), (UP, LEFT, RIGHT),
     (DOWN, LEFT, RIGHT)],  # 4번 CCTV
    [(UP, DOWN, LEFT, RIGHT)],  # 5번 CCTV
]


def get_cctv_dir_product(cctv_categories):
    product_list = []
    for cctv_category in cctv_categories:
        product_list.append(CCTV_DIR_CANDIDATES[cctv_category])
    return list(product(*product_list))


def is_valid(x, y, graph):
    # 범위안에 있고, 빈 곳이거나 이미 감시대상인 곳
    if 0 <= x < N and 0 <= y < M and graph[x][y] != 6:  # CCTV는 통과 가능
        return True
    return False


def fill(x, y, directions, graph):
    for direction in directions:
        copied_x, copied_y = x, y
        dx, dy = DX_DY[direction]
        while is_valid(copied_x + dx, copied_y + dy, graph):
            if graph[copied_x + dx][copied_y + dy] == 0: # cctv 아니면
                  graph[copied_x + dx][copied_y + dy] = WATCHABLE
            copied_x, copied_y = copied_x + dx, copied_y + dy


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

cctv_info = OrderedDict()
for i in range(N):
    for j in range(M):
        if 1 <= graph[i][j] <= 5:  #CCTV
            cctv_info[(i, j)] = graph[i][j]

cctv_directions = get_cctv_dir_product(cctv_info.values())  # 4**8
ans = float('inf')
for cctv_direction in cctv_directions:
    # {(1, 1): (0, 1), (3, 4): (0, 1), (5, 5): (0, 1, 2, 3)}
    dir_match = {
        key: dir
        for key, dir in zip(cctv_info.keys(), cctv_direction)
    }
    copied_graph = deepcopy(graph)  # 원본 초기화
    for i in range(N):
        for j in range(M):
            if (i, j) in dir_match:
                directions = dir_match[(i, j)]
                # 채우기 처리
                fill(i, j, directions, copied_graph)

    # 사각지대 수 측정해서 갱신 (8*8)
    empty_count = 0
    for i in range(N):
        for j in range(M):
            if copied_graph[i][j] == 0:
                empty_count += 1
    ans = min(ans, empty_count)
    # if ans == 9:
    #   for l in copied_graph:
    #     print(l)

print(ans)
