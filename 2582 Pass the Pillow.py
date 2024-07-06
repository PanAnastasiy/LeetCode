
class Solution(object):

    @staticmethod
    def passThePillow(n: int, time: int) -> int:
        if n > time:
            return time + 1
        elif time // (n - 1) % 2:
            return n - time % (n - 1)
        else:
            return time % (n - 1) + 1


print(Solution.passThePillow(4, 5))
