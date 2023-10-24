class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match_dict = dict()
        for i, num in enumerate(nums):
            if target-num in match_dict:
                return [i,match_dict[target-num]]
            match_dict[num] = i