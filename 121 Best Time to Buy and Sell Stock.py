class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = float('inf')
        high = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                high = max(high, prices[i] - low)
        return high


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
