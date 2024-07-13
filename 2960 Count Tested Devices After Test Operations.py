from typing import List


class Solution(object):

    @staticmethod
    def countTestedDevices(batteryPercentages: List[int]) -> int:
        total = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                total += 1
                batteryPercentages[i + 1:] = [max(0, batteryPercentages[j] - 1)
                                              for j in range(i + 1, len(batteryPercentages))]
        return total


print(Solution.countTestedDevices([0, 1, 2]))
