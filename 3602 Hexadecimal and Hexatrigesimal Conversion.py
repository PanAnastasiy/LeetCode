class Solution:
    def concatHex36(self, n: int) -> str:
        def toBase(n, base) -> str:
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ''
            while n > 0:
                result += digits[n % base]
                n //= base
            return result[::-1]
        return toBase(n**2, 16) + toBase(n**3, 36)



