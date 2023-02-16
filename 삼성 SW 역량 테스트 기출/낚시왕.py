import sys
input = sys.stdin.readline

UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4
DX_DY = [None, (-1, 0), (1, 0), (0, 1), (0, -1)]


def change_direction(dir):  # 방향 전환
    if dir == UP:
        return DOWN
    elif dir == DOWN:
        return UP
    elif dir == LEFT:
        return RIGHT
    elif dir == RIGHT:
        return LEFT
    else:
        print("error")


def is_valid(x, y):  # 격자 범위 안에 있는지
    if 0 <= x < R and 0 <= y < C:
        return True
    return False


class Shark:
    def __init__(self, r, c, s, d, z):
        self.x = r # 인덱스 0부터
        self.y = c # 인덱스 0부터
        self.speed = s
        self.direction = d  # 1(UP),2(DOWN),3(RIGHT),4(LEFT)
        self.size = z

    def move(self):  # 1초 후
        if self.direction in [LEFT, RIGHT]:
            self.speed %= ((C - 1) * 2)
        else:  # UP,DOWN
            self.speed %= ((R - 1) * 2)

        for _ in range(self.speed):  # 이만큼 이동 위에서 나머지해서 max 99
            dx, dy = DX_DY[self.direction]
            if is_valid(self.x + dx, self.y + dy):
                self.x, self.y = self.x + dx, self.y + dy
            else:
                # Direction 바꾸고 이동
                self.direction = change_direction(self.direction)
                dx, dy = DX_DY[self.direction]
                self.x, self.y = self.x + dx, self.y + dy


R, C, M = map(int, input().split())

sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r, c = r - 1, c - 1  # 인덱스 0기준으로
    sharks.append(Shark(r, c, s, d, z))

ans = 0
for remove_y_idx in range(C):  # 0~C-1
    # 1. 해당 열 중 가장 위에 있는 상어 제거
    sharks.sort(key=lambda shark: (shark.x))  # 처음발견된게 행이 가장 작도록
    for i, shark in enumerate(sharks):
        if shark.y == remove_y_idx:
            #print(shark.x + 1, shark.y + 1, shark.size, " 잡음")
            ans += shark.size
            sharks.pop(i)
            break

    # 2. 상어 이동
    for shark in sharks:
        shark.move()

    # 3. 같은 위치에 상어 여러개면 큰 것만 남기기
    new_sharks = []
    check_x_y = set()
    sharks.sort(key=lambda shark: -shark.size)  # 크기 큰게 무조건 먼저
    for shark in sharks:
        if (shark.x, shark.y) in check_x_y:
            #print(shark.x + 1, shark.y + 1, " 잡아먹힘")
            continue  # 이미 있으면
        new_sharks.append(shark)
        check_x_y.add((shark.x, shark.y))
    sharks = new_sharks

print(ans)

# for shark in sharks:
#   shark.move()

# for shark in sharks:
#   print(shark.x+1, shark.y+1, shark.direction)
