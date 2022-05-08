N = int(input())
nums = list(map(int, input().split()))
dp = [1 for _ in range(N)]  # 하나만 있는 수열이면 길이 1이므로

for i in range(1, N):
    for j in range(0, i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))