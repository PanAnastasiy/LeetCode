class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(list(str(num)))
        num1 = ''
        num2 = ''
        for i in range(0, len(digits)):
            if len(num1) <= len(num2):
                num1 += digits[i]
            else:
                num2 += digits[i]
        print(num1, num2)
        return int(num1) + int(num2)


print(Solution().splitNum(4325))
print(Solution().splitNum(687))