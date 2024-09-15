class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        total = 0
        for cost in sorted(costs):
            if coins >= cost:
                total += 1
                coins -= cost
            else:
                return total
        return total


sol = Solution()
print(sol.maxIceCream([10,6,8,7,7,8], 5))