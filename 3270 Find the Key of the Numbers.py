class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        key = []
        nums = list(map(lambda x: list((str(x)[::-1] + '0' * (4 - len(str(x))))), [num1, num2, num3]))
        for digit in zip(*nums):
            key.append(min(digit))
        return int(''.join(key[::-1]))


sol = Solution()
print(sol.generateKey(1, 10, 1000))
