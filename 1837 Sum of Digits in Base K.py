class Solution:
    def sumBase(self, n: int, k: int) -> int:
        new_number = []
        while n > 0:
            new_number.append(n % k)
            n //= k
        return sum(new_number)


print(Solution().sumBase(10, 10))