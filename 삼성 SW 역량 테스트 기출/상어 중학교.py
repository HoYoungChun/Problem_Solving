from collections import deque

EMPTY, BLACK, RAINBOW = -2, -1, 0
DX_DY = [(0,1),(1,0),(0,-1),(-1,0)]

def is_valid(i,j):
    """범위에 있는지만 체크"""
    if 0<=i<N and 0<=j<N:
        return True
    return False

def one_d_move(one_list):
    """1차원 리스트에서 왼쪽으로 중력 작용"""
    for from_idx in range(1,N):
        pass



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
            if graph[i][j] > 0: # 일반블록
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

    # TODO 중력 작용

    # !반시계 회전
    graph = list(map(list, zip(*graph)))[::-1]

    # TODO 중력 작용

    break # 디버깅용

print(score)