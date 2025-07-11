class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            stone_1 = stones.pop()
            stone_2 = stones.pop()
            if stone_1 != stone_2:
                stones.append(abs(stone_1 - stone_2))
        return stones[0] if stones else 0


print(Solution().lastStoneWeight([7, 6, 7, 6, 9]))
