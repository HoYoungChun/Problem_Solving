from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 누적합 배열 계산해두기
        cum_list = [0, nums[0]]
        for num in nums[1:]:
            cum_list.append(cum_list[-1] + num)

        # 이후는 two sum 문제와 비슷하나 등장횟수를 세어줘야 한다.(경우의 수를 세야 하니)
        ans = 0
        cnt_dict = defaultdict(int)  # 숫자: 등장횟수
        for cum_num in cum_list:
            if cum_num - k in cnt_dict:
                ans += cnt_dict[cum_num - k]
            cnt_dict[cum_num] += 1

        return ans