# 2022/10/05 00:05시작 01:00 AC 처리
# 문제: https://www.acmicpc.net/problem/16235
# 블로그 풀이: https://velog.io/@hozero/BOJ-16235%EB%B2%88-%EB%82%98%EB%AC%B4-%EC%9E%AC%ED%85%8C%ED%81%AC-Python-%EC%82%BC%EC%84%B1-SW-%EC%97%AD%EB%9F%89-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B8%B0%EC%B6%9C-%EB%AC%B8%EC%A0%9C


if __name__ == "__main__":
    from collections import defaultdict

    def is_valid(x,y):
        if 0<=x<N and 0<=y<N:
            return True
        return False
    
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]

    N,M,K = map(int,input().split())

    # A는 겨울마다 추가되는 양분의 양
    A = [list(map(int, input().split())) for _ in range(N)]
    
    # 초기 양분은 모두 5
    nutrient = [[5]*N for _ in range(N)]

    tree_info = defaultdict(list)
    for _ in range(M):
        x,y,z = map(int, input().split())
        x,y = x-1, y-1 # 인덱스에 맞게 변경
        tree_info[(x,y)] = [z] # 모두 다른 좌표로 처음에 주어진다
        # append 되는 값이 항상 어리다(항상 내림차순)

    for _ in range(K):
        die_tree_info = []
        # 봄
        for (x,y), age_list in tree_info.items():
            for i in reversed(range(len(age_list))): # 나이적은 순서대로
                if age_list[i] <= nutrient[x][y]:
                    nutrient[x][y] -= age_list[i] # 나이만큼 양분먹고
                    age_list[i] += 1 # 나이 1증가
                else:
                    die_tree_info.append((x,y,i,age_list))
                    break
        #print("봄 적용 후: ", tree_info)

        # 여름
        for x,y,i,age_list in die_tree_info:
            tree_info[(x,y)] = age_list[i+1:] # 죽는 나무 제외하고
            for age in age_list[:i+1]:
                nutrient[x][y] += age//2
        #print("여름 적용 후: ", tree_info)

        # 가을
        add_tree_info = []
        for (x,y), age_list in tree_info.items():
            for age in age_list:
                if age%5==0: # 번식
                    for i in range(8):
                        new_x = x + dx[i]
                        new_y = y + dy[i]
                        if is_valid(new_x, new_y):
                            add_tree_info.append((new_x,new_y))
        for x, y in add_tree_info:
            tree_info[(x,y)].append(1)
        #print("가을 적용 후: ", tree_info)

        # 겨울
        for i in range(N):
            for j in range(N):
                nutrient[i][j] += A[i][j]
    
    print(sum(len(x) for x in tree_info.values()))