from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        ans = ''
        for key in sorted(c.items(), key=lambda x: (-x[1], x[0])):
            ans += key[0] * key[1]
        return ans


print(Solution().frequencySort("tree"))