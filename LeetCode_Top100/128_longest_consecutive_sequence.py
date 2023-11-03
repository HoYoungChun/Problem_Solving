class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        num_set = set(nums)  # in, not in 연산을 O(1)로 처리하기 위해 set으로 형변환

        for num in num_set:  # O(N)
            if (num - 1) not in num_set:  # 연속되는 수들의 첫 시작 숫자일 때
                now_len = 1
                while (num + now_len) in num_set:
                    now_len += 1
                ans = max(ans, now_len)

        return ans