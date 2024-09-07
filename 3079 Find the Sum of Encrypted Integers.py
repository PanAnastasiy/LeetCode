from functools import reduce
class Solution:
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        return reduce(lambda x, y: x + y, [Solution.encrypt(num) for  num in nums], 0)

    @staticmethod
    def encrypt(number: int) -> int:
        return int(max(str(number)) * len(str(number)))


sol = Solution()
print(sol.sumOfEncryptedInt([10, 21, 31]))
