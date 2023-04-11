from collections import deque

N, K = map(int, input().split())
durabilites = deque(list(map(int, input().split())))
robots = deque([]) # durabilities의 인덱스를 저장(0~2N-1), 항상 오름차순된다!

step = 1
while True:
    # 1. 벨트가 로봇과 함께 회전
    durabilites.appendleft(durabilites.pop())
    robots = [robot+1 for robot in robots if (robot+1) !=(N-1)] # 내리는 위치에 도달한 로봇 제거
        

    # 2. 로봇 이동(이때도 내리는 위치 도달하면 내린다)
    new_robots=deque([])
    for robot in reversed(robots):
        if (robot+1) not in new_robots and durabilites[robot+1] >= 1:
            durabilites[robot+1] -= 1 # 로봇 이동했으니 내구도 감소
            if robot+1 == N-1: # 내리는 칸이면 내리기
                continue
            else:
                new_robots.appendleft(robot+1) # 한칸 이동
        else:
            new_robots.appendleft(robot) # 이동X
    robots = new_robots

    # 3. 올리는 위치에 로봇 올리기
    if durabilites[0] > 0:
        robots.appendleft(0)
        durabilites[0] -= 1


    # 4. durabilities에서 0이 k개 이상이면 과정 종료
    if durabilites.count(0) >= K: # 시간복잡도 최적화 필요
        break

    step += 1 # step 1 증가


print(step)