class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        if str(num)[-1] != '0':
            return True
        else:
            return False


print(Solution().isSameAfterReversals(526))
print(Solution().isSameAfterReversals(1800))
