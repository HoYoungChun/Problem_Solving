from collections import deque


DX_DY_4 = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def is_valid(x,y):
    """범위 안에 있는지"""
    if 0 <= x < 2**N and 0 <= y < 2**N:
        return True
    return False


def decrease():
    decrease_i_j = []
    for i in range(2**N):
        for j in range(2**N):
            cnt = 0
            for dx, dy in DX_DY_4:
                nx = i + dx
                ny = j + dy
                if is_valid(nx, ny) and A[nx][ny]:
                    cnt += 1

            if A[i][j] and cnt < 3:  # !!!얼음인 곳만
                decrease_i_j.append((i, j)) # !!! for문을 돌때 줄이면 안됨!!

    for i, j in decrease_i_j:
        A[i][j] -= 1 # for문을 돌때 줄이면 안됨!!


def rotate(L):
    """회전시키기"""
    dist = 2**L # 한변의 길이
    for i in range(0, 2**N, 2**L):
        for j in range(0, 2**N, 2**L):
            before_ratate = [one_list[j:j+dist] for one_list in A[i:i+dist]]
            after_roate = list(zip(*before_ratate[::-1]))

            for x in range(dist):
                for y in range(dist):
                    A[i+x][j+y] = after_roate[x][y]


def bfs(i,j):
    """(i,j)에서 연결된 덩어리가 차지하는 수 반환"""
    cnt = 1
    visited[i][j] = True
    queue = deque([(i, j)])

    while queue:
        x, y = queue.pop()
        for dx, dy in DX_DY_4:
            nx = x + dx
            ny = y + dy
            if is_valid(nx, ny) and not visited[nx][ny] and A[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1

    return cnt


N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2**N)]
L_list = list(map(int, input().split()))

for L in L_list:  # 2**L X 2**L으로 나누기

    # 1. 시계방향 회전
    rotate(L)

    # 2. 얼음양 1 감소
    decrease()

# for l in A:
#     print(l)

# 3. 남아있는 얼음 합
print(sum(sum(l) for l in A))

# TODO 4. 가장 큰 덩어리가 차지하는 칸의 개수 => BFS
visited = [[False]*(2**N) for _ in range(2**N)]
ans = 0 # !!!덩어리 없었을 때 결과 반환
for i in range(2**N):
    for j in range(2**N):
        if not visited[i][j] and A[i][j]: #!!!A[i][j] 조건 빠뜨림
            now_size = bfs(i, j)
            ans = max(ans, now_size)

print(ans)
