class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        sorted_prices = sorted(prices)
        price_choco = sorted_prices[0] + sorted_prices[1]
        if price_choco <= money:
            return money - price_choco
        else:
            return money


print(Solution().buyChoco([1, 2, 2], 3))
print(Solution().buyChoco([3, 2, 3], 3))