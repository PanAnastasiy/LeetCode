from functools import reduce


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        lst = list(map(int, str(n)))
        total = sum(lst) + reduce(lambda x, y: x * y, lst, 1)
        return n % total == 0


print(Solution().checkDivisibility(99))