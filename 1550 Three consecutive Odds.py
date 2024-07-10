from typing import List


class Solution(object):

    @staticmethod
    def threeConsecutiveOdds(arr: List[int]) -> bool:
        return len(max(''.join(list(map(lambda x: str(x) if x % 2 else 'X', arr))).split('X'), key=len)) > 2


print(Solution.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
