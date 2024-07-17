
class Solution:

    @staticmethod
    def sumOfTheDigitsOfHarshadNumber(x: int) -> int:
        total = sum(list(map(int, str(x))))
        return total if not x % total else -1


print(Solution.sumOfTheDigitsOfHarshadNumber(23))
