from collections import defaultdict

class Fireball:
    dx_dy = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

    def __init__(self,r,c,m,s,d):
        # 인덱스 0부터로 들어옴
        self.r = r # 행
        self.c = c # 열
        self.m = m # 질량
        self.s = s # 속력
        self.d = d # 방향
    
    def move(self):
        # s방향으로 d만큼 이동
        dx, dy = Fireball.dx_dy[self.d]
        self.r = (self.r + self.s*dx) % N
        self.c = (self.c + self.s*dy) % N
    
    def merge_fireballs(msd_list):
        # msd_list: [(m,s,d),...]
        m_sum = sum(msd[0] for msd in msd_list)
        s_sum = sum(msd[1] for msd in msd_list)
        is_even_set = set(d%2==0 for _,_,d in msd_list) # {True}
        new_ds = [0,2,4,6] if len(is_even_set)==1 else [1,3,5,7]

        new_m = int(m_sum/5)
        new_s = int(s_sum/len(msd_list))

        if new_m == 0:
            return [] # 질량 0이면 소멸
        
        new_msd_list = []
        for new_d in new_ds:
            new_msd_list.append((new_m,new_s,new_d))

        return new_msd_list

    def __str__(self) -> str: # 디버깅용
        return f"{self.r} {self.c} {self.m} {self.s} {self.d}"

N, M, K = map(int, input().split())

fireballs = []
for _ in range(M):
    r,c,m,s,d = map(int, input().split())
    r,c = r-1,c-1 # 인덱스 0부터 하기 위해
    fireballs.append(Fireball(r,c,m,s,d))

for _ in range(K):
    # 1. 이동
    for fireball in fireballs:
        fireball.move()
    
    # 2. 같은 칸에 있는 파이어볼들 4개로 나누기
    rc_msd_dict = defaultdict(list) # {(r,c):[(m,s,d),...], ...}
    for fb in fireballs:
        r,c,m,s,d = fb.r,fb.c,fb.m,fb.s,fb.d
        rc_msd_dict[(r,c)].append((m,s,d))

    new_fireballs = []
    for rc,msd_list in rc_msd_dict.items():
        r,c = rc

        if len(msd_list) >= 2: # 2개 이상 있을때 4개로 쪼개기
            next_msd_list = Fireball.merge_fireballs(msd_list)
        else:
            next_msd_list = msd_list
        
        for m,s,d in next_msd_list:
            new_fireballs.append(Fireball(r,c,m,s,d))

    fireballs = new_fireballs

print(sum(fb.m for fb in fireballs)) # 질량합