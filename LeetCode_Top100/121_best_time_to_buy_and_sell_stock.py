class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]

        for price in prices:
            ans = max(ans, price - min_price)  # ans 갱신(profit이 음수여도 ans초기값 0이라서 괜찮다)
            min_price = min(min_price, price)  # min_price 갱신

        return ans