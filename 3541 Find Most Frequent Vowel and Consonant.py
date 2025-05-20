class Solution:
    def maxFreqSum(self, s: str) -> int:
        dct_1 = {}
        dct_2 = {}
        for char in set(s):
            if char in ('a', 'e', 'i', 'o', 'u'):
                dct_1[char] = s.count(char)
            else:
                dct_2[char] = s.count(char)
        max_1 = max(dct_1.values()) if dct_1 else 0
        max_2 = max(dct_2.values()) if dct_2 else 0
        return max_1 + max_2


print(Solution().maxFreqSum('successes'))
print(Solution().maxFreqSum('aeiaeia'))
