from itertools import product
from copy import deepcopy

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3


def move_left(one_list):  # one_list를 왼쪽으로 밈
    merged = [False] * len(one_list)  # 합쳐진 블록인지 여부

    for i in range(1, len(one_list)):  # 왼쪽부터 하니씩 왼쪽으로 땡기기(1, 2, ..., N-1)
        reach_end = True

        for j in reversed(range(i)):  # i-1, i-2, ..., 0
            if one_list[j] == 0:  # 빈칸
                continue
            elif one_list[j] == one_list[i] and not merged[j]:  # 합치기
                one_list[j] *= 2
                merged[j] = True
                one_list[i] = 0
                reach_end = False
                break  #옮겼으니 탈출
            else:  # 멈출 위치
                one_list[j + 1] = one_list[i]
                if j + 1 != i:  # 같을 수 있다
                    one_list[i] = 0
                reach_end = False
                break

        # 맨끝도달
        if reach_end:
            one_list[0] = one_list[i]
            one_list[i] = 0

    return one_list  # 민 결과 반환 (call by reference여서 반환값 필요하면 받기)


def board_one_move(copied_board, direction):
    if direction == UP:
        for i in range(N):  # 세로줄 하나씩
            one_list = [garo[i] for garo in copied_board]
            return_list = move_left(one_list)
            for idx, num in enumerate(return_list):
                copied_board[idx][i] = num

    elif direction == DOWN:
        for i in range(N):  # 세로줄 하나씩
            one_list = [garo[i] for garo in copied_board]
            return_list = move_left(one_list[::-1])[::-1]
            for idx, num in enumerate(return_list):
                copied_board[idx][i] = num

    elif direction == LEFT:
        for i in range(N):  # 가로줄 하나씩
            move_left(copied_board[i])

    else:  # RIGHT
        for i in range(N):  # 가로줄 하나씩
            copied_board[i] = move_left(copied_board[i][::-1])[::-1]


N = int(input())  # 보드 크기
board = [list(map(int, input().split())) for _ in range(N)]
ans = -float('inf')

for directions in product([UP, DOWN, LEFT, RIGHT], repeat=5):
    copied_board = deepcopy(board)  # 보드 복제

    # 5번 이동
    for direction in directions:
        board_one_move(copied_board, direction)

    # 최대값 갱신
    for i in range(N):
        for j in range(N):
            ans = max(ans, copied_board[i][j])

print(ans)
