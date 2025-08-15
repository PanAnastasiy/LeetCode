from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4) % 1 <= 10**(-9)


print(Solution().isPowerOfFour(5))
