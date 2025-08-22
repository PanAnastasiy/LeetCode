from collections import Counter


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        c = Counter(arr)
        target = len(arr) // 4
        for key, value in c.items():
            if value >= target:
                return value
