from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우,하,좌,상


def is_valid(x, y, body):
    if 0 <= x < N and 0 <= y < N and (x, y) not in body:  # O(N)
        return True
    return False


class Snake:
    def __init__(self):
        self.body = deque([(0, 0)])  # 오른쪽이 머리, 왼쪽이 꼬리
        self.dir_idx = 0  # 방향(처음엔 오른쪽)


N = int(input())  # 보드 크기
graph = [[False] * N for _ in range(N)]  # 보드(True면 사과 존재)

K = int(input())  # 사과의 개수
for _ in range(K):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = True  # 인덱스 0부터로

L = int(input())  # 방향 전환 정보 개수
move_on_sec = dict()  # 각 초가 끝난 뒤 방향 전환 정보 저장
for _ in range(L):
    X, C = input().split()
    move_on_sec[int(X)] = C

snake = Snake()
for sec in range(1, 10001):  # 1~10000초

    # 이동하려는 곳에 내 몸이 있거나 벽이면 게임 종료
    dx, dy = DIRECTIONS[snake.dir_idx]
    x, y = snake.body[-1] # 머리
    move_x, move_y = x + dx, y + dy
    if not is_valid(move_x, move_y, snake.body):
        print(sec)
        break

    # 이동(사과 처리)
    snake.body.append((move_x, move_y))  # 머리 이동
    if graph[move_x][move_y]:  # 사과 있으면
        graph[move_x][move_y] = False
    else:
        snake.body.popleft()  # 꼬리 이동

    # 방향 전환
    if sec in move_on_sec:
        if move_on_sec[sec] == 'L':  # 좌
            snake.dir_idx -= 1
        else:  # 우
            snake.dir_idx += 1

        snake.dir_idx %= 4  # 인덱스 에러 방지
