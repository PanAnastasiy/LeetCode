
class Solution(object):

    @staticmethod
    def countOperations(n, m) -> int:
        total = 0
        while n and m:
            if n > m:
                n -= m
            else:
                m -= n
            total += 1
        return total

print(Solution.countOperations(2,3))
