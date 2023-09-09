from collections import defaultdict

# 상수 정의
RIGHT, LEFT, UP, DOWN = 1, 2, 3, 4
WHITE, RED, BLUE = 0, 1, 2
dx_dy = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]


# 함수 정의
def is_valid(x, y):
    """범위안에 들어있고 파란색 아닌지 체크"""
    if 0 <= x < N and 0 <= y < N and maps[x][y] != BLUE:
        return True
    return False


def reverse_direction(dir):
    if dir == RIGHT: return LEFT
    elif dir == LEFT: return RIGHT
    elif dir == UP: return DOWN
    elif dir == DOWN: return UP


def move_horse(horse_num:int):
    """horse_num에 해당하는 이동을 수행"""
    #print(horse_num)
    #print(horse_location)

    # 말에 해당하는 좌표 찾기
    now_x, now_y = None, None
    for x_y, horse_nums in horse_location.items():
        if horse_num in horse_nums:
            now_x, now_y = x_y

    dx, dy = dx_dy[horse_direction[horse_num]]
    new_x, new_y = now_x + dx, now_y + dy

    if is_valid(new_x, new_y) and maps[new_x][new_y] == WHITE:  # 흰색
        # 슬라이싱해서 이동하는 좌표에 append & 기존꺼 제거
        idx = horse_location[(now_x, now_y)].index(horse_num)
        horse_location[(new_x, new_y)].extend(horse_location[(now_x, now_y)][idx:])
        horse_location[(now_x, now_y)] = horse_location[(now_x, now_y)][:idx]

    elif is_valid(new_x, new_y) and maps[new_x][new_y] == RED:  # 빨간색
        # 슬라이싱 후 뒤집이서 이동하는 좌표에 append & 기존꺼 제거
        idx = horse_location[(now_x, now_y)].index(horse_num)
        horse_location[(new_x, new_y)].extend(horse_location[(now_x, now_y)][idx:][::-1])
        horse_location[(now_x, now_y)] = horse_location[(now_x, now_y)][:idx]

    else:  # 외부 or 파란색
        # 방향 뒤집고 그쪽도 파&외부 아니면 move_horse 호출
        horse_direction[horse_num] = reverse_direction(horse_direction[horse_num])
        dx, dy = dx_dy[horse_direction[horse_num]]
        new_x, new_y = now_x + dx, now_y + dy
        if is_valid(new_x, new_y):
            move_horse(horse_num)

    if len(horse_location[(now_x,now_y)]) == 0:  # 비었을 때
        del horse_location[(now_x, now_y)]


# 메인
horse_direction = dict()
horse_location = defaultdict(list)

N, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, K+1):
    input_x, input_y, direction = map(int, input().split())
    x, y = input_x-1, input_y-1

    horse_direction[i] = direction
    horse_location[(x, y)].append(i)

turn_cnt = 1
while turn_cnt <= 1000:
    # 말 이동 & 4개 이상 쌓이면 종료
    for horse_num in range(1, K+1):
        move_horse(horse_num)  # 말 이동

        # 4개 이상 쌓였는 지 체크
        for horse_nums in horse_location.values():
            if len(horse_nums) >= 4:
                print(turn_cnt)
                exit()

    turn_cnt += 1

print(-1)
