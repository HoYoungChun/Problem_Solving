from collections import deque
CLOCKWISE, COUNTER_CLOCKWISE = 1, -1

def move(queue, direction):
  if direction == CLOCKWISE: # 시계 방향
    queue.appendleft(queue.pop())
  else: # 반시계 방향
    queue.append(queue.popleft())

def is_valid(q_num, visited):
  if 1<=q_num<=4 and not visited[q_num]: # 1~4번에 해당하면서 돌린적(방문한적) 없을때
    return True
  return False

def queue_move(q_num, direction, visited):
  visited[q_num] = True # 방문처리

  # 왼쪽 톱니바퀴
  if is_valid(q_num-1, visited) and queues[q_num-1][2] != queues[q_num][6]:
    queue_move(q_num-1, direction*(-1), visited)   

  # 오른쪽 톱니바퀴
  if is_valid(q_num+1, visited) and queues[q_num][2] != queues[q_num+1][6]:
    queue_move(q_num+1, direction*(-1), visited)
      
  move(queues[q_num], direction) # 돌리기 이전 기준으로 왼쪽, 오른쪽 체크하므로 맨 마지막에 돌리기

queue1 = deque(map(int, list(input())))
queue2 = deque(map(int, list(input())))
queue3 = deque(map(int, list(input())))
queue4 = deque(map(int, list(input())))
queues = [None, queue1, queue2, queue3, queue4] # 인덱싱 번호랑 같게 편하게 하려고 1부터

K = int(input())
for _ in range(K):
  queue_num, direction = map(int, input().split())
  visited = [False]*5
  queue_move(queue_num, direction, visited)

# 점수 합 구해서 출력
print(queue1[0]*1+queue2[0]*2+queue3[0]*4+queue4[0]*8)
