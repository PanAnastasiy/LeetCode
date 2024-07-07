
class Solution(object):

    @staticmethod
    def numWaterBottles(numBottles: int, numExchange: int) -> int:
        total, empty = 0, 0
        while numBottles > 0:
            total += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty -= numExchange * numBottles
        return total


print(Solution.numWaterBottles(15, 4))
