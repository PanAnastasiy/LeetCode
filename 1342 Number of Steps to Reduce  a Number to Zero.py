
class Solution:

    @staticmethod
    def numberOfSteps(n: int) -> int:
        total = 0
        while n:
            if n % 2:
                n -= 1
            else:
                n //= 2
            total += 1
        return total


print(Solution.numberOfSteps(123))
