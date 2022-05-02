def solution(places):
    answer = []
    
    for one_place in places:
        is_distance_okay = distance_check(one_place) # 한 place마다 계산
        answer.append(is_distance_okay)
    
    return answer


def distance_check(one_place):
    for i in range(5):
        for j in range(5):
            if one_place[i][j]=="P":
                if distance_false_person_exists(one_place,i,j):
                    return 0
    return 1 # 거리두기 모두 잘 지킴


def distance_false_person_exists(one_place,i,j):
    if j<4 and one_place[i][j+1]=="P":
        return True
    elif i<4 and one_place[i+1][j]=="P":
        return True
    
    
    elif j<3 and one_place[i][j+2]=="P" and one_place[i][j+1]=="O":
        return True
    elif i<3 and one_place[i+2][j]=="P" and one_place[i+1][j]=="O":
        return True
    
    
    elif i<4 and j<4 and one_place[i+1][j+1]=="P" and (one_place[i][j+1]=="O" or one_place[i+1][j]=="O"):
        return True
    elif i<4 and j>0 and one_place[i+1][j-1]=="P" and (one_place[i][j-1]=="O" or one_place[i+1][j]=="O"):
        return True # 대각선 역방향도 고려!
    else:
        return False
