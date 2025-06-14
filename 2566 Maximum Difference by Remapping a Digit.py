class Solution:
    def minMaxDifference(self, num: int) -> int:
        number = str(num)
        maxi = num
        for digit in number:
            if digit != '9':
                maxi = int(number.replace(digit, '9'))
                break
        mini = int(number.replace(number[0], '0'))
        return maxi - mini


print(Solution().minMaxDifference(11891))
