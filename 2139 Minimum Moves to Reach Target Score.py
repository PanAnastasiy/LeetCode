
class Solution:

    @staticmethod
    def minMoves(target: int, maxDoubles: int) -> int:
        counter = 0
        while target != 1:
            if target % 2:
                target -= 1
            elif maxDoubles:
                target //= 2
                maxDoubles -= 1
            else:
                return counter + target - 1
            counter += 1
        return counter


print(Solution.minMoves(656101987, 1))
