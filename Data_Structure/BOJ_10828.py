# https://www.acmicpc.net/problem/10828

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline  # 시간초과 막기 위해
    N = int(input())
    stack = []

    for _ in range(N):
        command = input().split()
        if command[0] == "push":
            stack.append(command[1])
        elif command[0] == "pop":
            print(stack.pop()) if stack else print(-1)
        elif command[0] == "size":
            print(len(stack))
        elif command[0] == "empty":
            print(1) if not stack else print(0)
        elif command[0] == "top":
            print(stack[-1]) if stack else print(-1)
        else:  # 문제조건으로 여기 올 일 없다
            pass
