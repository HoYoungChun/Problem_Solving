# 2022/10/03 16:00 시작, 17:00 AC
# 문제: https://www.acmicpc.net/problem/16234
# 블로그 풀이: https://velog.io/@hozero/BOJ-16234%EB%B2%88-%EC%9D%B8%EA%B5%AC-%EC%9D%B4%EB%8F%99-Python

if __name__ == "__main__":
    from collections import deque
    import sys

    input = sys.stdin.readline # 시간초과 방지용

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    def is_valid(x,y):
        if 0<=x<N and 0<=y<N:
            return True
        return False

    def bfs(x ,y, is_visited):
        union = {(x,y)}
        queue = deque([[x,y]])
        is_visited[x][y] = True
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if is_valid(new_x, new_y) and not is_visited[new_x][new_y] and L<=abs(A[x][y]-A[new_x][new_y])<=R:
                    union.add((new_x,new_y))
                    queue.append((new_x, new_y))
                    is_visited[new_x][new_y] = True
        return union

    N,L,R = map(int, input().split())
    A = [list(map(int,input().split())) for _ in range(N)]

    answer = 0
    while True:
        find_union = False
        is_visited = [[False]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not is_visited[i][j]:
                    union = bfs(i,j,is_visited)
                    if len(union) >=2: # 2개 이상 지역이 연합
                        find_union = True

                        # 인구 갱신
                        change_population = int(sum(A[x][y] for x,y in union) / len(union)) # 버림
                        for x, y in union:
                            A[x][y] = change_population

        if find_union: # 인구이동 일어났으면(한턴에 여러번 발생하는 것도 하나로 처리해야함)
            answer += 1
        
        if not find_union:
            break

    print(answer)