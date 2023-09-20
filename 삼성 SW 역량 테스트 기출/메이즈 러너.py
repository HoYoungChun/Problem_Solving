
def move_people():
    """사람들 이동(total_distance 추가, 목적지 도달하면 제거)"""
    distance = 0
    for i, x_y in enumerate(people):
        x, y = x_y

        # 상하 방향 먼저 체크
        if exit_x < x and maze[x-1][y] == 0:  # 위
            people[i] = (x-1, y)
            distance += 1

        elif exit_x > x and maze[x+1][y] == 0:  # 아래
            people[i] = (x+1, y)
            distance += 1

        # 좌우 방향 이후 체크
        elif exit_y < y and maze[x][y-1] == 0:  # 왼
            people[i] = (x, y-1)
            distance += 1

        elif exit_y > y and maze[x][y+1] == 0:  # 오른
            people[i] = (x, y+1)
            distance += 1
    
    # 목적지 도달 제거
    new_people = []
    for i, x_y in enumerate(people):
        x, y = x_y
        if (x, y) != (exit_x, exit_y):
            new_people.append((x,y))

    return distance, new_people


def rotate_x_y(rx, ry, rd, x, y):
    """(rx,ry)를 좌상단 좌표로 하는 길이 rd의 정사각형을 회전할 때
    상대적 좌표 기준의 (x,y)의 변경될 좌표"""
    if 0 <= x < rd and 0 <= y < rd:
        return rx+y, ry+rd-1-x

    return None, None  # 이런 경우가 들어오면 안됨!


def find_rx_ry_rd():
    # rx, ry, rd 찾기 (rx 좌표 작고, ry좌표 작은 순)
    for rd in range(1, N + 1):  # 한변 크기(1 ~ N)
        for rx in range(0, N - rd + 1):
            for ry in range(0, N - rd + 1):
                people_include = False
                for px, py in people:
                    if rx <= px < rx + rd and ry <= py < ry + rd:
                        people_include = True

                if people_include and (rx <= exit_x < rx + rd and ry <= exit_y < ry + rd):
                    # 출구 포함 & 참가자 최소 1명 포함 체크
                    return rx, ry, rd

    return rx, ry, rd


# 미로 크기, 참가자수, 게임시간
N, M, K = map(int, input().split())

# 0: 빈칸, 1~9: 벽
maze = [list(map(int, input().split())) for _ in range(N)]
people = []

for _ in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1  # 인덱스 1기준으로 주어졌으니
    people.append((x, y))

# 출구 좌표
exit_x, exit_y = map(int, input().split())
exit_x, exit_y = exit_x - 1, exit_y - 1

total_distance = 0  # 모든 참가자들의 이동 거리 합
for _ in range(K):

    # 1. 모든 참가자 이동(easy)
    distance, people = move_people()
    total_distance += distance

    if not people:  # 모든 참가자 탈출
        break

    # 2. 미로 회전
    # 2-1. 가장 작은 정사각형 찾기 - 참가자마다 정사각형 하나씩 제작
    rx, ry, rd = find_rx_ry_rd()

    # 2-2. 90도 회전(maze, people, exit_x_y 변경)
    # 2차원 배열 커팅
    before_rotate_arr = [one_list[ry:ry+rd] for one_list in maze[rx:rx+rd]]
    # 90도 회전한 결과 받기
    after_roate_arr = list(map(list, zip(*before_rotate_arr[::-1])))
    # 커팅된 부분에 다시 넣기
    for i in range(rd):
        for j in range(rd):
            maze[rx+i][ry+j] = after_roate_arr[i][j]

    for i, x_y in enumerate(people):
        x, y = x_y
        if rx <= x < rx+rd and ry <= y < ry+rd:
            people[i] = rotate_x_y(rx, ry, rd, x-rx, y-ry)

    exit_x, exit_y = rotate_x_y(rx, ry, rd, exit_x-rx, exit_y-ry)

    # 2-3. 회전한 벽 내구도 1 감소(easy)
    for i in range(rd):
        for j in range(rd):
            if maze[rx+i][ry+j] > 0:
                maze[rx + i][ry + j] -= 1


    # print(people)
    # print(exit_x, exit_y)
    # for l in maze:
    #     print(l)
    # print()


# 정답 출력
print(total_distance)
print(exit_x+1, exit_y+1)  # 인덱스 1부터로 출력해야 함
