
class Solution:
    @staticmethod
    def maximum69Number(num: int) -> int:
        num = list(str(num))
        if '6' in num:
            num[num.index('6')] = '9'
        return int(''.join(num))


print(Solution.maximum69Number(969))
