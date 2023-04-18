from collections import deque

EMPTY, BLACK, RAINBOW = -float('inf'), -1, 0 # 1이상은 일반블록
DX_DY = [(0,1),(1,0),(0,-1),(-1,0)]

def print_graph(graph):
    """디버깅용"""
    for g in graph:
        print(g)

def is_valid(i,j):
    """범위에 있는지만 체크"""
    if 0<=i<N and 0<=j<N:
        return True
    return False

def two_d_move(graph):
    # 시계 회전
    graph = list(map(list,zip(*graph[::-1])))

    # 각 row별 1차원 중력 적용
    for g in graph:
        one_d_move(g)

    # 반시계 회전
    graph = list(map(list,zip(*graph)))[::-1]

    return graph

def one_d_move(one_list):
    """1차원 리스트에서 왼쪽으로 중력 작용"""
    for from_idx in range(1,N):
        if one_list[from_idx] >= 0:
            check_idx = from_idx -1
            while check_idx >= 0 and one_list[check_idx] == EMPTY:
                # SWAP
                one_list[check_idx],one_list[check_idx+1] = one_list[check_idx+1],one_list[check_idx]
                check_idx -= 1

def bfs(i,j):
    """(i,j) 일반블록에서 만들 수 있는 최대 블록 그룹 구해서 정보 반환"""
    # !EMPTY도 고려해야됨
    visited = [[False]*N for _ in range(N)]
    visited[i][j] = True
    block_group_ij_list = [(i,j)]
    queue = deque([(i,j)])
    same_color = graph[i][j]

    while queue:
        x,y = queue.pop()
        for dx, dy in DX_DY:
            check_x = x+dx
            check_y = y+dy
            if is_valid(check_x,check_y) and not visited[check_x][check_y]\
            and graph[check_x][check_y] in [RAINBOW, same_color]:
                visited[check_x][check_y] = True
                queue.appendleft((check_x,check_y))
                block_group_ij_list.append((check_x,check_y))

    # rainbow_cnt 구하기
    rainbow_cnt = sum(1 for i,j in block_group_ij_list if graph[i][j] == RAINBOW)

    # main_block_ij 구하기
    for i,j in sorted(block_group_ij_list): # (i,j) 오름차순
        if graph[i][j] > 0: # 일반 블록
            main_block_ij = (i,j)
            break
    
    return block_group_ij_list,rainbow_cnt, main_block_ij
    

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

score = 0

while True:
    block_cand = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0: # 일반&무지개블록
                ij_list, rainbow_cnt, main_blocK_ij = bfs(i,j)
                if len(ij_list) >= 2: # 블록 2개 이상이어야 블록그룹
                    block_cand.append((ij_list, rainbow_cnt, main_blocK_ij))
    
    if not block_cand: # 블록그룹 없으면 종료
        break

    block_cand.sort(key = lambda x: (-len(x[0]),-x[1],-x[2][0],-x[2][1]))

    delete_ij_list = block_cand[0][0] # 제거할 좌표들
    score += (len(delete_ij_list)**2) # 점수 획득

    # 제거하기
    for i, j in delete_ij_list:
        graph[i][j] = EMPTY

    # 중력 작용
    graph = two_d_move(graph)

    # !반시계 회전
    graph = list(map(list, zip(*graph)))[::-1]

    # 중력 작용
    graph = two_d_move(graph)

print(score)