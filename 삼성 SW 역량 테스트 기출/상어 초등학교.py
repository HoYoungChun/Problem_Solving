from collections import OrderedDict

EMPTY = -1
DX_DY = [(0,1),(0,-1),(1,0),(-1,0)]

def is_valid(r,c):
    """범위 안에 있는지만 체크(인덱스 0부터)"""
    if 0<=r<N and 0<=c<N:
        return True
    return False


N = int(input())
student_love_info = OrderedDict() # key인 학생순서 유지용
for _ in range(N**2):
    student_num, *love_info = map(int, input().split())
    student_love_info[student_num] = set(love_info)

seating = [[EMPTY]*N for _ in range(N)] # !인덱스 0부터

for student_num, love_info in student_love_info.items():
    seating_weights = [] # [(인접 좋아하는 학생수,인접 빈칸수,행,열),...]
    for i in range(N):
        for j in range(N):
            if seating[i][j] == EMPTY:
                love_cnt = 0 # 인접 좋아하는 학생 수
                empty_cnt = 0 # 인접 빈칸 수

                for dx,dy in DX_DY: # 인접 4방향 체크
                    check_x = i+dx
                    check_y = j+dy
                    if is_valid(check_x,check_y):
                        if seating[check_x][check_y] in love_info:
                            love_cnt += 1
                        elif seating[check_x][check_y] == EMPTY:
                            empty_cnt += 1
                    

                seating_weights.append((love_cnt, empty_cnt, i, j))

    seating_weights.sort(key = lambda x:(-x[0],-x[1],x[2],x[3]))
    _, _, next_r, next_c = seating_weights[0]
    seating[next_r][next_c] = student_num

# 가중치 구하기(자리배치하면서 구하면 안됨)
ans = 0
for i in range(N):
    for j in range(N):
        student_num = seating[i][j]
        love_cnt = 0
        for dx, dy in DX_DY:
            check_x = i+dx
            check_y = j+dy
            if is_valid(check_x,check_y):
                if seating[check_x][check_y] in student_love_info[student_num]:
                    love_cnt += 1
        
        if love_cnt >= 1:
            ans += (10**(love_cnt-1))

print(ans)