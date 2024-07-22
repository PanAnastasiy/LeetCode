# sum() -> 28
#   + (n % 7 * (n // 7))

class Solution(object):
    @staticmethod
    def totalMoney(n: int) -> int:
        a1 = sum([1, 2, 3, 4, 5, 6, 7][:n % 7])
        return int((28 + 3.5 * (n // 7 - 1)) * (n // 7) + a1 + (n % 7)*(n // 7))


print(Solution.totalMoney(20))

# + n % 7 + n // 7 - 1
