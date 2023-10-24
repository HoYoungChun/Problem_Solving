from collections import defaultdict

DX_DY_4 = [(0,1), (1,0), (0,-1), (-1,0)]


def find_max_height_x_y():
    """장 높은 봉우리들 위치 뽑기"""
    find_max_height_dict = defaultdict(list)
    for i in range(N):
        for j in range(N):
            find_max_height_dict[heights[i][j]].append((i, j))

    max_height_i_j = sorted(find_max_height_dict.items(), key=lambda x: -x[0])[0][1]
    return max_height_i_j


def is_valid(x, y):
    """범위 안에 있는지만 체크"""
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


def dfs(x, y, visited, now_len):
    # TODO 정답갱신
    global ans
    ans = max(ans, now_len)

    for dx, dy in DX_DY_4:
        nx = x + dx
        ny = y + dy
        if is_valid(nx, ny) and not visited[nx][ny] and heights[nx][ny] < heights[x][y]:
            visited[nx][ny] = True
            dfs(nx, ny, visited, now_len+1)
            visited[nx][ny] = False  # ! 꼭 원복

#import sys
#sys.stdin = open("input.txt", "r")


# 사용할 전역변수들
N, K = 0, 0
heights = [[]]
ans = float('-inf')

T = int(input())
for test_case in range(1, T + 1):
    # !전역 변수 초기화
    N, K = map(int, input().split())
    heights = [list(map(int, input().split())) for _ in range(N)]
    ans = float('-inf')  # 이 테스트 케이스에서의 최대 등산로 길이

    # ! 가장 높은 봉우리가 깎였을 수도 있어서 매번 찾아야됨
    max_height_i_j = find_max_height_x_y()

    for i in range(N):
        for j in range(N):
            for now_k in range(K+1):
                heights[i][j] -= now_k
                
                # ! 가장 높은 봉우리가 깎였을 수도 있어서 매번 찾아야됨
                # max_height_i_j = find_max_height_x_y()

                # 2.가장 높은 봉우리들마다 가장 긴 등산로길이 찾아서 갱신
                for max_i, max_j in max_height_i_j:
                    visited = [[False] * N for _ in range(N)]
                    visited[max_i][max_j] = True
                    dfs(max_i, max_j, visited, 1)  # dfs 수행하며 max_len 갱신

                heights[i][j] += now_k  # 다음 경우를 위해 원복

    print(f"#{test_case} {ans}")
