from functools import reduce


class Solution:

    def find_product(self, n) -> int:
        digits = list(map(int, str(n)))
        return reduce(lambda x, y: x * y, list(digits), 1)

    def smallestNumber(self, n: int, t: int) -> int:
        while self.find_product(n) % t != 0:
            n += 1
        return n


print(Solution().smallestNumber(10, 2))
print(Solution().smallestNumber(15, 3))