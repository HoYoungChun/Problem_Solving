from collections import deque


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        end_idx = 0
        farthest_idx = 0

        # Implicit BFS (Greedy BFS)
        for idx in range(n - 1):  # 0 ~ n-2 (n-1인덱스는 체크 안해도 됨)
            farthest_idx = max(farthest_idx, idx + nums[idx])  # 최대로 갈 수 있는 인덱스 위치
            if farthest_idx >= n - 1:  # 마지막 인덱스 도달 가능
                ans += 1
                break

            if idx == end_idx:  # visited all the items on the current level
                ans += 1  # Increment the level
                end_idx = farthest_idx  # Make the queue size for the next level

        return ans