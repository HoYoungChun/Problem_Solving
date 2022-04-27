# https://www.acmicpc.net/problem/9012

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline  # 시간초과 방지 위해
    T = int(input())

    for _ in range(T):
        stack_len = 0  # 스택의 길이
        ps = input()
        is_vps = True
        for parenthesis in ps:
            if parenthesis == "(":  # stack push
                stack_len += 1
            elif parenthesis == ")":  # stack pop
                stack_len -= 1
            else:  # (, ) 외에는 등장안하므로 여기 올 일 없다
                pass
            if stack_len < 0:  # VPS 탈락
                is_vps = False
                break

        if stack_len != 0:  # VPS 탈락
            is_vps = False

        print("YES") if is_vps else print("NO")
