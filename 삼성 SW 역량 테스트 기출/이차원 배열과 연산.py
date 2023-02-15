from collections import Counter


def counter_clockwise(graph):
    """2차원 배열 반시계 방향 회전한 배열 반환"""
    M = len(graph)
    N = len(graph[0])
    new_graph = []
    for j in reversed(range(N)):
        new_graph.append([graph[i][j] for i in range(M)])
    return new_graph


def unpack_tuple_to_list(line):
    """[(0,1),(2,3)] => [0,1,2,3]"""
    temp_list = []
    for l in line:
        if l[0] != 0:  # 0은 무시
            temp_list.append(l[0])
            temp_list.append(l[1])
    return temp_list


def op_R(graph):
    new_graph = []
    for line in graph:
        new_line = Counter(line).most_common()
        new_line.sort(key=lambda x: (x[1], x[0]))  # 등장횟수, 수
        new_line = unpack_tuple_to_list(new_line)
        new_graph.append(new_line)

    # 0 채우기
    max_len = max(len(l) for l in new_graph)
    for line in new_graph:
        while len(line) != max_len:
            line.append(0)

    return new_graph


r, c, k = map(int, input().split())
r, c = r - 1, c - 1  # 인덱스 0부터 읽게
A = [list(map(int, input().split())) for _ in range(3)]

# ANS
second = 0
while second <= 100:
    M = len(A)  # 행 개수
    N = len(A[0])  # 열 개수

    if 0 <= r < M and 0 <= c < N and A[r][c] == k:  # 인덱스 체크 필요
        print(second)
        break

    if M >= N:  # 행 >= 열
        A = op_R(A)
    else:
        # 반시계로 뒤집어서 op_R에 전달
        A = op_R(counter_clockwise(A))

        # 결과 시계 방향으로 뒤집어서 A에 저장(반시계3번==시계1번)
        for _ in range(3):
            A = counter_clockwise(A)

    second += 1

if second == 101:  # while문 끝까지 돌았으면
    print(-1)
