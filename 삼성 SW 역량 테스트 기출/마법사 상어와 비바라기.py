
DX_DY_8 = [None, (0, -1), (-1, -1), (-1, 0), (-1, 1),
         (0, 1), (1, 1), (1, 0), (1, -1)]

DX_DY_4 = [(1, 1), (-1, 1), (1, -1), (-1, -1)]


def is_valid(x, y):
    """범위 안에 있는지"""
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


def move_clouds(direction, s):
    """구름 이동"""
    dx, dy = DX_DY_8[direction]
    dx, dy = dx*s, dy*s
    for idx, cloud in enumerate(clouds):
        x, y = clouds[idx]
        new_x = (x + dx) % N
        new_y = (y + dy) % N
        clouds[idx] = (new_x, new_y)


def water_copy_magic():
    """물복사마법: 대각선에 물있는 수만큼 물 증가(경계 벗어나면 무시)"""
    for x, y in clouds:
        for dx, dy in DX_DY_4:
            check_x = x + dx
            check_y = y + dy
            if is_valid(check_x, check_y) and waters[check_x][check_y]:  # 범위안에 있고 물 있으면
                waters[x][y] += 1


N, M = map(int, input().split())
waters = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]  # 구름 좌표들

for _ in range(M):
    direction, s = map(int, input().split())

    # 1. 구름들 이동(!경계 벗어난거 포함)
    move_clouds(direction, s)

    # 2. 구름있는 칸 물 1 증가
    for x, y in clouds:
        waters[x][y] += 1

    # 3. 구름 제거 => 뒤에서 구름 생성하면서 덮어씌우기

    # 4. 물이 증가한 칸에 대해서 물복사버그 마법(!경계 벗어난거 미포함)
    water_copy_magic()

    # 5. 물 2이상인 곳 구름 생성(3에서 제거된게 아닌)
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if waters[i][j] >= 2 and ((i, j) not in clouds):
                new_clouds.append((i, j))
                waters[i][j] -= 2

    clouds = new_clouds

# M번 이동 후 바구니 물의 합 출력
print(sum(sum(one_list) for one_list in waters))
