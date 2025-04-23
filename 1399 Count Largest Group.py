from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        dct = defaultdict(list)
        for num in range(1, n + 1):
            total = sum(map(int, str(num)))
            dct[total].append(num)
        largest = len(max(dct.values(), key=len))
        return len(list((filter(lambda x: len(x) == largest, dct.values()))))


print(Solution().countLargestGroup(13))
