from collections import deque

DX_DY = [(-1,0),(0,1),(1,0),(0,-1)]
NORTH, EAST, SOUTH, WEST = 0,1,2,3 # +1은 시계방향,-1은 반시계방향
INVERSE_DIRECTION = {NORTH: SOUTH, EAST: WEST, SOUTH: NORTH, WEST: EAST}


class Dice:
    def __init__(self):
        # x,y 좌표(인덱스 0부터!)
        self.x = 0
        self.y = 0

        # 해당방향에 적힌 주사위 번호
        self.top = 1 # 위에서 보이는 윗면
        self.bottom = 6
        self.left = 4
        self.right = 3
        self.up = 2
        self.down = 5 # !6으로 잘못썼었다.

        # 방향
        self.direction = EAST # 처음은 동쪽

        # 점수
        self.score = 0
    
    def move(self):
        # 이동방향 막혀있으면 반대로 변경
        dx,dy = DX_DY[self.direction]
        move_x,move_y = self.x+dx, self.y+dy
        if not is_valid(move_x,move_y):
            self.direction = INVERSE_DIRECTION[self.direction]
        
        # 주사위 좌표 변경
        dx,dy = DX_DY[self.direction]
        self.x, self.y = self.x+dx, self.y+dy

        # 주사위 칸 번호 변경
        if self.direction == NORTH:
            self.top, self.up, self.bottom, self.down =\
                self.down, self.top, self.up, self.bottom
        elif self.direction == SOUTH:
            self.top, self.up, self.bottom, self.down =\
                self.up, self.bottom, self.down, self.top
        elif self.direction == EAST:
            self.top, self.right, self.bottom, self.left =\
                self.left, self.top, self.right, self.bottom
        elif self.direction == WEST:
            self.top, self.right, self.bottom, self.left =\
                self.right, self.bottom, self.left, self.top

def is_valid(x,y):
    """범위안에 있는지만(인덱스 0부터!)"""
    if 0<=x<N and 0<=y<M:
        return True
    return False

def get_connected_cnt(x,y):
    """(x,y)에서 같은수로 연결된 수 반환(BFS), O(N*M)"""
    visited = [[False]*M for _ in range(N)]
    cnt = 1 # (x,y)는 포함
    visited[x][y] = True
    queue = deque([(x,y)])

    while queue:
        x,y = queue.pop()
        for dx, dy in DX_DY:
            check_x = x+dx
            check_y = y+dy
            if is_valid(check_x,check_y) and not visited[check_x][check_y]\
                and graph[x][y] == graph[check_x][check_y]:
                cnt += 1
                visited[check_x][check_y] = True
                queue.appendleft((check_x,check_y))

    return cnt


N,M,K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dice = Dice()

# 1. 점수판 구하기(연결된 같은칸수)
score = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        connected_cnt = get_connected_cnt(i,j)
        score[i][j] += connected_cnt*graph[i][j]

# 2. 주사위 이동
for _ in range(K):
    # 주사위 이동(막히면 반대방향으로)
    dice.move()

    # 점수 획득
    dice.score += score[dice.x][dice.y]

    # 이동방향 결정
    A = dice.bottom
    B = graph[dice.x][dice.y]
    if A > B: # 시계방향
        dice.direction += 1
    elif A < B:
        dice.direction -= 1
    dice.direction %= 4


print(dice.score)