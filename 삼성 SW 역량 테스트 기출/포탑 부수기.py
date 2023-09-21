from collections import deque

DX_DY_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우 하 좌 상 순서
DX_DY_8 = [(0,1), (0,-1), (1, 1), (1,-1), (1,0), (-1,1), (-1,-1), (-1,0)]


def bfs():
    """레이저 공격 성공여부 + 경로 반환"""
    queue = deque([(attack_x, attack_y, [])])
    visited = [[False]*M for _ in range(N)]
    visited[attack_x][attack_y] = True

    while queue:
        x, y, path = queue.pop()
        if (x, y) == (defend_x, defend_y):
            return True, path

        for dx, dy in DX_DY_4:
            new_x = (x + dx) % N
            new_y = (y + dy) % M  # 반대편 나옴
            if arr[new_x][new_y] != 0 and not visited[new_x][new_y]:
                new_path = path + [(new_x, new_y)]
                visited[new_x][new_y] = True
                queue.appendleft((new_x, new_y, new_path)) # !appendleft해야됨

    return False, path  # 도달 못함


def find_attacker():
    """공격자 좌표 찾기"""
    sort_list = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                sort_list.append((i, j, arr[i][j], attack_history[i][j], i+j, j))

    sort_list.sort(key=lambda x: (x[2], -x[3], -x[4], -x[5]))

    return sort_list[0][0], sort_list[0][1]


def find_defender():
    """방어자 좌표 찾기(공격자와 달라야 함)"""
    sort_list = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and (i, j) != (attack_x, attack_y):
                sort_list.append((i, j, arr[i][j], attack_history[i][j], i+j, j))

    sort_list.sort(key=lambda x: (-x[2], x[3], x[4], x[5]))

    return sort_list[0][0], sort_list[0][1]


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
attack_history = [[0]*M for _ in range(N)]

# 부서지지 않은 포탑이 1개가 된다면 그 즉시 중단
for turn_num in range(K):
    # 1. 공격자 선정
    attack_x, attack_y = find_attacker()
    attack_history[attack_x][attack_y] = turn_num+1  # 마지막으로 공격한 턴 저장(!!!K로 잘못적었었음)
    arr[attack_x][attack_y] += (N+M) # 공격력 상승

    # 2-1. 공격받는 포탑(방어자) 선정 (!공격자 제외)
    defend_x, defend_y = find_defender()

    # 2-2. 레이저 공격 시도
    lazer_success, path = bfs()  # 도달하면 success 반환

    # !path에는 공격자는 제외, 방어자는 포함되어 있음

    # 2-3. 레이저 공격 실패시 포탄 공격
    if not lazer_success:
        path = [(defend_x, defend_y)]
        for dx, dy in DX_DY_8:
            new_x = (defend_x + dx) % N
            new_y = (defend_y + dy) % M  # 반대편 나옴
            if arr[new_x][new_y] != 0 and (new_x, new_y) != (attack_x, attack_y):  # 공격자 제외
                path.append((new_x, new_y))

    # defender와 path 경로에 있는 곳 피해 주기
    for x, y in path:
        if (x, y) == (defend_x, defend_y):
            arr[x][y] -= arr[attack_x][attack_y]
        else:
            arr[x][y] -= (arr[attack_x][attack_y] // 2)  # 절반 피해

        if arr[x][y] < 0: # 음수되면 0으로
            arr[x][y] = 0 

    # 3. 포탑 부서짐 => break 조건 체크
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cnt += 1
    if cnt == 1:
        break

    # 4. 포탑 정비(공격과 무관한 포탑들 공격력 +=1)
    for i in range(N):
        for j in range(M):
            # !!! arr[i][j] !=0 조건 빼먹었음
            if arr[i][j] != 0 and (i, j) != (attack_x, attack_y) and (i, j) not in path:
                arr[i][j] += 1

# 남아 있는 포탑 중 가장 강한 포탑 공격력 출력
ans = -float('inf')
for i in range(N):
    for j in range(M):
        if arr[i][j] > ans:
            ans = arr[i][j]
print(ans)
