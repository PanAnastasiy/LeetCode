class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        index = 0
        for i in range(len(num) - 1, -1, -1):
            if num[i] != '0':
                index = i
                break
        return num[:index + 1]


print(Solution().removeTrailingZeros("51230100"))
print(Solution().removeTrailingZeros("123"))
