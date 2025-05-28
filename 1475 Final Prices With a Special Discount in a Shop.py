class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    stack.append(prices[i] - prices[j])
                    break
            else:
                stack.append(prices[i])
        return stack


print(Solution().finalPrices([8, 4, 6, 2, 3]))
print(Solution().finalPrices([1, 2, 3, 4, 5]))
