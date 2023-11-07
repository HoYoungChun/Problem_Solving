class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # 지금 온도보다 작았던 곳들 정답 갱신
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                ans[idx] = i - idx

            stack.append(i)  # (index)

        return ans