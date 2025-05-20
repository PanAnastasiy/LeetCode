class Solution:
    def maxProduct(self, n: int) -> int:
        lst = sorted([int(i) for i in str(n)])
        return lst[-1] * lst[-2]


print()
