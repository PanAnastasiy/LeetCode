class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(str(num))
        print(num[0] + num[2], num[1] + num[3])
        return int(num[0] + num[2]) + int(num[1] + num[3])


print(Solution().minimumSum(4009))
print(Solution().minimumSum(2932))


