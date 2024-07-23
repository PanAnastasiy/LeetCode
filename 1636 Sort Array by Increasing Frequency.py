from typing import List


class Solution:

    def frequencySort(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (arr.count(x), -x))


sol = Solution()
print(sol.frequencySort([1, 1, 2, 2, 2, 3]))
print(sol.frequencySort([2, 3, 1, 3, 2]))
