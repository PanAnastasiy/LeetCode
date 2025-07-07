class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        length = len(s)
        n = s.count('1')
        return '1' * (n - 1) + '0' * (length - n) + '1'
