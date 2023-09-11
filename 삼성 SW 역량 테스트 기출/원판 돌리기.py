from collections import deque

dx_dy = [(0,1),(0,-1),(1,0),(-1,0)]


def is_valid(x,y):
    """범위 안에 있는지"""
    if 0<=x<N and 0<=y<M:
        return True
    return False


def bfs(x, y, visited):
    target_num = maps[x][y] # None 아닌것만 전달됨
    queue = deque([(x, y)])
    near_x_y_list = [(x, y)]
    visited[x][y] = True

    while queue:
        now_x, now_y = queue.pop()
        for dx, dy in dx_dy:
            new_x, new_y = now_x + dx, now_y + dy
            if new_y < 0:  # 음수 처리
                new_y += M
            elif new_y >= M: # 초과 처리(!처음에 못찾음)
                new_y -= M

            if is_valid(new_x, new_y) and maps[new_x][new_y] \
                    and maps[new_x][new_y] == target_num and not visited[new_x][new_y]:
                visited[new_x][new_y] = True # 방문처리
                queue.append((new_x, new_y))
                near_x_y_list.append((new_x, new_y))

    return near_x_y_list


def rotate(x,d,k):
    """x의 배수인 원판을 d방향으로 k번 이동시키기"""
    for i in range(N):
        if ((i+1) % x) == 0:  # x의 배수번째
            for _ in range(k):
                if d == 0:  # 시계방향
                    maps[i].appendleft(maps[i].pop())
                else:  # 반시계 방향
                    maps[i].append(maps[i].popleft())


def rebalancing():
    """전체원판에 적힌 수 기준 평균에서 더하고 빼기"""
    valid_nums = []
    for i in range(N):
        for j in range(M):
            if maps[i][j]:  # None인건 제거된거
                valid_nums.append(maps[i][j])

    if len(valid_nums) == 0:
        return # 모두 None이면(!처음에 못찾음)

    avg = sum(valid_nums) / len(valid_nums)

    for i in range(N):
        for j in range(M):
            if maps[i][j]:  # None인건 제거된거
                if maps[i][j] > avg:
                    maps[i][j] -= 1
                elif maps[i][j] < avg:
                    maps[i][j] += 1


N, M, T = map(int, input().split())
maps = [deque(map(int, input().split())) for _ in range(N)]
x_d_k = [list(map(int, input().split())) for _ in range(T)]


for x, d, k in x_d_k:  # O(50)
    # 1. x의 배수인 원판을 d방향으로 k번 이동시키기
    rotate(x, d, k)

    # 2. 원판에서 인접하면서 같은수 쭉 찾기
    total_near_x_y_list = []
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if maps[i][j] and not visited[i][j]:
                near_x_y_list = bfs(i, j, visited)
                # print(near_x_y_list)
                if len(near_x_y_list) >= 2:
                    total_near_x_y_list.append(near_x_y_list)

    # print(total_near_x_y_list)

    # 2-1. 인접하면서 같은 수 모두 지우기
    if len(total_near_x_y_list) >= 1:
        for near_x_y_list in total_near_x_y_list:
            for x, y in near_x_y_list:
                maps[x][y] = None
    else:  # 2-2. 인접하면서 같은 수 없으면 평균 구해서 평균기준 1더하고 빼기
        rebalancing()

    #print(total_near_x_y_list)
    #(maps)

sum = 0
for i in range(N):
    for j in range(M):
        if maps[i][j]:
            sum += maps[i][j]
print(sum)