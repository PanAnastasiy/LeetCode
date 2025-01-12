class Solution:

    def prefixCount(self, words: list[str], pref: str) -> int:
        index = len(pref)
        return len(list(filter(lambda w: w[:index] == pref, words)))


print(Solution().prefixCount(["pay", "attention", "practice", "attend"], "at"))
