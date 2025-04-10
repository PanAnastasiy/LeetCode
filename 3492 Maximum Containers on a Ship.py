class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(n * n, maxWeight // w)


print(Solution().maxContainers(2, 3, 15))
print(Solution().maxContainers(3, 5, 20))
