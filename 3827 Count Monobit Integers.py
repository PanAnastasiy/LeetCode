from math import log, floor


class Solution:
    def countMonobit(self, n: int) -> int:
        l = floor(log(n, 2))
        print(l)
        return l + 1


print(Solution().countMonobit(1))