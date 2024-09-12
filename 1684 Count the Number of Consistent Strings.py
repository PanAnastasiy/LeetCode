class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        total = len(words)
        for word in words:
            for char in set(word):
                if char not in allowed:
                    total -= 1
                    break
        return total


sol = Solution()
print(sol.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))
