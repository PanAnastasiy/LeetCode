from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        maximum = -1
        minimum = len(s)
        for value in c.values():
            if value % 2:
                maximum = max(value, maximum)
            else:
                minimum = min(value, minimum)
        return maximum - minimum


print(Solution().maxDifference("abcabcab"))
