class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i, num in enumerate(nums):
            if i <= max_index:
                max_index = max(max_index, i+num)

        if max_index >= len(nums)-1: # 마지막 인덱스보다 크거나 같으면 도달 가능
            return True
        return False