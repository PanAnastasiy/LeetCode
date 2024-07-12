from typing import List


class Solution(object):

    @staticmethod
    def separateDigits(n: List[int]) -> List[int]:
        return list(map(int, list(''.join(map(str, n)))))


print(Solution.separateDigits([13, 25, 83, 77]))
