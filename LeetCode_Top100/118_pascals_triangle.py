class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        nums = [1]

        for _ in range(numRows - 1):
            new_nums = [nums[0]]
            for i in range(len(nums) - 1):
                new_nums.append(nums[i] + nums[i + 1])
            new_nums.append(nums[-1])

            ans.append(new_nums)
            nums = new_nums

        return ans
