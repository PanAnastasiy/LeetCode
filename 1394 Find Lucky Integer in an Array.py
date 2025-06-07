class Solution:
    def findLucky(self, arr: list[int]) -> int:
        dct = {a: arr.count(a) for a in arr}
        for key, value in sorted(dct.items(), reverse=True):
            if key == value:
                return value
        return -1
