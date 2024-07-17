
class Solution(object):

    @staticmethod
    def countDigits(n: int) -> int:
        temp, total = n, 0
        while temp:
            print(n, temp)
            if n % (temp % 10) == 0:
                total += 1
            temp //= 10
        return total



print(Solution.countDigits(1248))
