class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (low % 2 and high % 2 or low % 2 or high % 2)
