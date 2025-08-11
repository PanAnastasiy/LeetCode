class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort(reverse=True)
        total = 0
        for i in range(0, len(piles) * 2 // 3, 2):
            total += piles[i + 1]
        return total