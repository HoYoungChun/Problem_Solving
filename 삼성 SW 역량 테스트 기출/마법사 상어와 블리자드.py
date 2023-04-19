EMPTY = -float('inf')
DX_DY = [0,(-1,0),(1,0),(0,-1),(0,1)] # d(방향)에 대응


def print_graph(graph):
    """디버깅용"""
    for g in graph:
        print('\t'.join(map(str,g)))

def destroy(d,s):
    """d방향으로 s거리만큼 구슬파괴"""
    dx,dy = DX_DY[d]
    cx,cy = shark_x,shark_y
    for _ in range(s):
        cx,cy = cx+dx,cy+dy
        graph[cx][cy] = EMPTY

def get_graph_move_ij():
    graph_move_ij=[]
    for make_size in range(3,N+1,2): # 3,5,7,..
        graph_move_ij.extend([(0,-1)]) # 왼쪽
        graph_move_ij.extend([(1,0)]*(make_size-2)) # 아래
        graph_move_ij.extend([(0,1)]*(make_size-1)) # 오른쪽
        graph_move_ij.extend([(-1,0)]*(make_size-1)) # 위
        graph_move_ij.extend([(0,-1)]*(make_size-1)) # 왼쪽
    return graph_move_ij

def graph_to_list(graph):
    """graph를 칸 번호 순대로 list형태로 반환"""
    one_list = []

    cx,cy = shark_x, shark_y
    for dx, dy in graph_move_ij:
        cx = cx+dx
        cy = cy+dy
        one_list.append(graph[cx][cy])

    return one_list

def list_to_graph(one_list):
    """칸 번호 순대로인 list를 graph로 반환"""
    new_graph = [[EMPTY]*N for _ in range(N)]
    cx,cy = shark_x, shark_y
    for idx, (dx,dy) in enumerate(graph_move_ij):
        cx = cx+dx
        cy = cy+dy
        new_graph[cx][cy] = one_list[idx]
    
    return new_graph

def marble_move(one_list):
    """왼쪽으로 빈칸 없애면서 이동"""
    for from_idx in range(1,len(one_list)):
        target_idx = from_idx-1
        while target_idx >=0 and one_list[target_idx]==EMPTY:
            one_list[target_idx], one_list[target_idx+1] = one_list[target_idx+1], one_list[target_idx]
            target_idx-=1


N,M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
ds_list = [list(map(int,input().split())) for _ in range(M)]

# 빈곳 EMPTY로 설정(!상어위치도 EMPTY로)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = EMPTY

shark_x = shark_y = (N-1)//2 # 상어좌표
graph_move_ij = get_graph_move_ij()

for d,s in ds_list:
    # 1. 구슬파괴(빈칸생성)
    destroy(d,s)

    # graph -> list
    one_list = graph_to_list(graph)
    print(one_list)

    # 2. 구슬이동(앞으로 당기기)
    marble_move(one_list)

    # TODO 3. 구슬폭발(빈칸생성) 불가능할때까지 => 정답갱신

    # TODO 4. 구슬변화
    
    # graph -> list
    graph = list_to_graph(one_list)

    break