from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer–Moore majority vote algorithm
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:  # candidate 탈락
                candidate = num

            if num == candidate:  # candidate가 또 등장하면
                count += 1
            else:
                count -= 1

        return candidate
