
class Solution(object):

    @staticmethod
    def commonFactors(a: int, b: int) -> int:
        total = 1
        for num in range(2, min(a, b) + 1):
            if a % num == 0 and b % num == 0:
                total += 1
        return total


print(Solution.commonFactors(25, 30))
