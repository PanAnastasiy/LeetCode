class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolor = k
        if 'B' * k in blocks:
            return 0
        for index in range(0, len(blocks) - k + 1):
            print(blocks[index:index + k])
            white_blocks = blocks[index: index + k].count('W')
            if white_blocks < min_recolor:
                min_recolor = white_blocks
        return min_recolor


print(Solution().minimumRecolors("WBBWWBBWBW", 7))
print(Solution().minimumRecolors("BWWWBB", 6))
print(Solution().minimumRecolors("WWBBBWBBBBBWWBWWWB", 16))