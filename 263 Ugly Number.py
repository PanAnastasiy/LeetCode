class Solution:

    def isUgly(self, n: int) -> bool:
        while n and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0):
            if not n % 2:
                n = n // 2
            elif not n % 3:
                n = n // 3
            else:
                n = n // 5
        return True if n == 1 else False
