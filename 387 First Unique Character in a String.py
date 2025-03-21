class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct = {ch: s.count(ch) for ch in set(s)}
        for ch in s:
            if dct[ch] == 1:
                return s.index(ch)
        return -1


print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar("aabb"))
