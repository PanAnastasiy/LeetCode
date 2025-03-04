from math import log


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            power = log(n, 3)
            print(power)
            return abs(round(power) - power) < 0.00000000001
        return False


print(Solution().isPowerOfThree(27))
print(Solution().isPowerOfThree(243))
print(Solution().isPowerOfThree(-1))
