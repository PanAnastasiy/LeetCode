
# (2*a0 + d(n - 1)) * n / 2

class Solution:

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = (4 + 2 * (n - 1)) * n // 2
        even = (2 + 2 * (n - 1)) * n // 2
        return self.gcd(odd, even)


print(Solution().gcdOfOddEvenSums(4))
