#시간초과
def solution(n, k, cmd):
    bool_table = [True for _ in range(n)]
    selected_idx = k
    exist_max_idx = n-1
    deleted_idx_list = []
    
    
    for one_cmd in cmd:
        splited_cmd = one_cmd.split()
        
        if splited_cmd[0]=="Z":
            deleted_idx = deleted_idx_list.pop()
            bool_table[deleted_idx] = True
            exist_max_idx = max(exist_max_idx,deleted_idx)
            
        elif splited_cmd[0]=="C":
            deleted_idx_list.append(selected_idx)
            bool_table[selected_idx] = False
            if selected_idx == exist_max_idx:
                while not bool_table[selected_idx]: # 다음이 False일 수 있다!
                    selected_idx -= 1
                exist_max_idx = selected_idx
            else:
                while not bool_table[selected_idx]: # 다음이 False일 수 있다!
                    selected_idx += 1
        
        elif splited_cmd[0]=="U":
            distance = int(splited_cmd[1])
            while distance != 0:
                selected_idx -= 1
                if bool_table[selected_idx]:
                    distance -= 1
        
        elif splited_cmd[0]=="D":
            distance = int(splited_cmd[1])
            while distance != 0:
                selected_idx += 1
                if bool_table[selected_idx]:
                    distance -= 1

    return "".join(["O" if x else "X" for x in bool_table])
