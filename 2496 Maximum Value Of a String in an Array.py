from typing import List


class Solution:

    @staticmethod
    def maximumValue(arr: List[str]) -> int:
        lst = list(map(lambda x: int(x) if x.isdigit() else len(x), arr))
        return max(lst)


Solution.maximumValue(["alic3", "bob", "3", "4", "00000"])
