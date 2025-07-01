from collections import Counter


class Solution:
    def checkPrimeFrequency(self, nums: list[int]) -> bool:
        dct = Counter(nums)
        for num in sorted(dct.values()):
            if self.isPrime(num):
                return True
        return False

    def isPrime(self, n: int) -> bool:
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
