class Solution:
    def isFascinating(self, n: int) -> bool:
        digits = str(n) + str(n * 2) + str(n * 3)
        return ''.join(sorted(digits)) == '123456789'


print(Solution().isFascinating(192))
