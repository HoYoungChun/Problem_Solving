from itertools import combinations

EMPTY, HOUSE, BBQ = 0, 1, 2

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


all_house_list = []
all_bbq_list = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == HOUSE:
            all_house_list.append((i, j))
        elif graph[i][j] == BBQ:
            all_bbq_list.append((i, j))

ans = float('inf')
for bbq_list in combinations(all_bbq_list, M):
    now_total_distance = 0
    for hx, hy in all_house_list:
        now_total_distance += min(
            get_distance(hx, hy, bx, by) for bx, by in bbq_list)

    ans = min(ans, now_total_distance)

print(ans)
