class Dice:
    # 주사위 정보 초기화
    def __init__(self, x, y):
        self.x = x  # x좌표(0~N-1)
        self.y = y  # y좌표(0~N-1)
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        self.sky = 0  # 상단
        self.bottom = 0  # 하단

    # 한번에 다중할당 안하면 변경된 값이 할당될 수 있어서 순서를 매우 유의해야 함.
    def move_east(self):  # 동쪽으로 굴리기
        self.bottom, self.right, self.sky, self.left = \
        self.right, self.sky, self.left, self.bottom

    def move_west(self):  # 서쪽으로 굴리기
        self.bottom, self.right, self.sky, self.left = \
        self.left, self.bottom, self.right, self.sky

    def move_north(self):  # 북쪽으로 굴리기
        self.bottom, self.up, self.sky, self.down  = \
        self.up, self.sky, self.down, self.bottom

    def move_south(self):  # 남쪽으로 굴리기
        self.bottom, self.up, self.sky, self.down  = \
        self.down, self.bottom, self.up, self.sky


def is_valid(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False


EAST, WEST, NORTH, SOUTH = 1, 2, 3, 4
dxdy = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]

N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))

dice = Dice(x, y)
for move in moves:
    # 이동가능한지 체크하고 이동 안되면 continue
    dx, dy = dxdy[move]
    new_x, new_y = dice.x + dx, dice.y + dy
    if not is_valid(new_x, new_y):
        continue

    # 주사위 이동
    if move == EAST:
        dice.move_east()
    elif move == WEST:
        dice.move_west()
    elif move == NORTH:
        dice.move_north()
    else:  # SOUTH
        dice.move_south()

    # 주사위 좌표 변경
    dice.x, dice.y = new_x, new_y

    # 윗면 출력
    print(dice.sky)

    # 주사위 바닥, 지도 비교
    moved_x, moved_y = dice.x, dice.y
    if graph[moved_x][moved_y] == 0:
        graph[moved_x][moved_y] = dice.bottom  # 주사위 => 지도
    else:
        dice.bottom = graph[moved_x][moved_y]
        graph[moved_x][moved_y] = 0
