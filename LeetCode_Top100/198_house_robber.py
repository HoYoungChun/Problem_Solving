class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n  # dp[k]: k번쨰 house까지의 최대 rob 합

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for idx in range(2, n):
            dp[idx] = max(dp[idx - 1], dp[idx - 2] + nums[idx])  # idx를 포함할때, 포함하지 않을때

        return dp[n - 1]