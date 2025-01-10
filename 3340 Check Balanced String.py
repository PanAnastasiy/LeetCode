
class Solution:
    def isBalanced(self, num: str) -> bool:
        result_sum = 0
        for i in range(len(num)):
            if i % 2:
                result_sum += int(num[i])
            else:
                result_sum -= int(num[i])
        return not result_sum


print(Solution().isBalanced("24123"))
