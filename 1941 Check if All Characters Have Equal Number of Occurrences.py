class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hash_map = {t: s.count(t) for t in set(s)}
        return len(set(hash_map.values())) == 1


print(Solution().areOccurrencesEqual(str("abacbc")))