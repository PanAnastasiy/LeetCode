from typing import List


class Solution:

    @staticmethod
    def sumOddLengthSubarrays(arr: List[int]) -> int:
        total = 0
        for n in range(len(arr)):
            for i in range(n % 2, len(arr), 2):
                total += sum(arr[n:i + 1])
        return total


print(Solution.sumOddLengthSubarrays([10,11,12]))
