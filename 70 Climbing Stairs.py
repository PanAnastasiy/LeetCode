"""
class Solution(object):

    @staticmethod
    def climbStairs(n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return Solution.climbStairs(n - 1) + Solution.climbStairs(n - 2)

"""


class Solution(object):

    @staticmethod
    def climbStairs(n: int) -> int:
        first, second = 0, 1
        for i in range(n):
            first, second = second, first + second
        return second


print(Solution.climbStairs(6))

