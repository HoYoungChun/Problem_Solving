UP = [['w'] * 3 for _ in range(3)]
DOWN = [['y'] * 3 for _ in range(3)]
FRONT = [['r'] * 3 for _ in range(3)]
BACK = [['o'] * 3 for _ in range(3)]
LEFT = [['g'] * 3 for _ in range(3)]
RIGHT = [['b'] * 3 for _ in range(3)]

DIR_LEFT, DIR_RIGHT, DIR_UP, DIR_DOWN = 0, 1, 2, 3


def init_case():
    global UP, LEFT, BACK, RIGHT, FRONT, DOWN
    UP = [['w'] * 3 for _ in range(3)]
    DOWN = [['y'] * 3 for _ in range(3)]
    FRONT = [['r'] * 3 for _ in range(3)]
    BACK = [['o'] * 3 for _ in range(3)]
    LEFT = [['g'] * 3 for _ in range(3)]
    RIGHT = [['b'] * 3 for _ in range(3)]


def get_real_xy(direction, fakex, fakey):
    """direction방향을 위쪽으로 생각해서 (fakex,fakey)의 진짜 좌표 3*3기준"""
    if direction == DIR_UP:
        return fakex, fakey
    elif direction == DIR_LEFT:
        return 2 - fakey, fakex
    elif direction == DIR_RIGHT:
        return fakey, 2 - fakex
    else:  # DIR_DOWN
        return 2 - fakex, 2 - fakey


def move(s1, d1, s2, d2, s3, d3, s4, d4):
    # s1 <- s2, s2<-s3, s3<-s4, s4<-s1 방향으로 이동
    for x, y in [(0, 0), (0, 1), (0, 2)]:
        rx1, ry1 = get_real_xy(d1, x, y)
        rx2, ry2 = get_real_xy(d2, x, y)
        rx3, ry3 = get_real_xy(d3, x, y)
        rx4, ry4 = get_real_xy(d4, x, y)
        s1[rx1][ry1], s2[rx2][ry2], s3[rx3][ry3], s4[rx4][ry4] \
      = s2[rx2][ry2], s3[rx3][ry3], s4[rx4][ry4], s1[rx1][ry1]


def roatate(arr, dir):
    new_arr = [[0] * 3 for _ in range(3)]
    if dir == "+":  # 시계방향
        direction = DIR_LEFT
    else:
        direction = DIR_RIGHT

    for i in range(3):
        for j in range(3):
            new_i, new_j = get_real_xy(direction, i, j)
            new_arr[i][j] = arr[new_i][new_j]

    return new_arr


def rotation_itself(method):
    global UP, LEFT, BACK, RIGHT, FRONT, DOWN
    if method[0] == 'U':
        UP = roatate(UP, method[1])
    elif method[0] == "L":
        LEFT = roatate(LEFT, method[1])
    elif method[0] == "B":
        BACK = roatate(BACK, method[1])
    elif method[0] == "R":
        RIGHT = roatate(RIGHT, method[1])
    elif method[0] == "F":
        FRONT = roatate(FRONT, method[1])
    elif method[0] == "D":
        DOWN = roatate(DOWN, method[1])


def move_method(methods):
    for method in methods:
        # 돌리는 판 자체도 돌려줘야함.
        rotation_itself(method)

        if method == "L+":
            move(FRONT, DIR_LEFT, UP, DIR_LEFT, BACK, DIR_RIGHT, DOWN,
                 DIR_LEFT)
        elif method == "L-":
            move(DOWN, DIR_LEFT, BACK, DIR_RIGHT, UP, DIR_LEFT, FRONT,
                 DIR_LEFT)
        elif method == "U+":
            move(FRONT, DIR_UP, RIGHT, DIR_UP, BACK, DIR_UP, LEFT, DIR_UP)
        elif method == "U-":
            move(LEFT, DIR_UP, BACK, DIR_UP, RIGHT, DIR_UP, FRONT, DIR_UP)
        elif method == "F+":
            move(RIGHT, DIR_LEFT, UP, DIR_DOWN, LEFT, DIR_RIGHT, DOWN, DIR_UP)
        elif method == "F-":
            move(DOWN, DIR_UP, LEFT, DIR_RIGHT, UP, DIR_DOWN, RIGHT, DIR_LEFT)
        elif method == "B+":
            move(UP, DIR_UP, RIGHT, DIR_RIGHT, DOWN, DIR_DOWN, LEFT, DIR_LEFT)
        elif method == "B-":
            move(LEFT, DIR_LEFT, DOWN, DIR_DOWN, RIGHT, DIR_RIGHT, UP, DIR_UP)
        elif method == "R+":
            move(UP, DIR_RIGHT, FRONT, DIR_RIGHT, DOWN, DIR_RIGHT, BACK,
                 DIR_LEFT)
        elif method == "R-":
            move(BACK, DIR_LEFT, DOWN, DIR_RIGHT, FRONT, DIR_RIGHT, UP,
                 DIR_RIGHT)
        elif method == "D+":
            move(RIGHT, DIR_DOWN, FRONT, DIR_DOWN, LEFT, DIR_DOWN, BACK,
                 DIR_DOWN)
        elif method == "D-":
            move(BACK, DIR_DOWN, LEFT, DIR_DOWN, FRONT, DIR_DOWN, RIGHT,
                 DIR_DOWN)
        else:
            print("method 잘못됨")


n = int(input())
for _ in range(n):
    num = int(input())  # 안씀
    init_case()  # 각 면 초기화
    methods = input().split()
    move_method(methods)

    for line in UP:
        print(''.join(line))
