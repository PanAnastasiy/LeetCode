from typing import List


class Solution:

    @staticmethod
    def canAliceWin(nums: List[int]) -> bool:
        total = 0
        for num in nums:
            if num < 10:
                total -= num
            else:
                total += num
        return total != 0


print(Solution.canAliceWin([5, 5, 5, 25]))
