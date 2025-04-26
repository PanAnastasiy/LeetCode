from typing import List

# (min(numbers[i - 1][0] + numbers[i - 2][0], key=numbers[i - 1][1] + numbers[i - 2][1])


class Solution(object):

    @staticmethod
    def minCostClimbingStairs(cost: List[int]) -> int:
        dp = [cost[-1], cost[-2]]
        for i in range(len(cost) - 3, -1, -1):
            dp.append(cost[i] + min(dp[-1], dp[-2]))
        return min(dp[-1], dp[-2])


print(Solution.minCostClimbingStairs([10, 15, 20]))
print(Solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))