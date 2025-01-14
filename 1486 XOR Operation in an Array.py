from functools import reduce


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2*i for i in range(n)]
        return reduce(lambda x, y: x ^ y, nums, 0)


print(Solution().xorOperation(4, 3))
