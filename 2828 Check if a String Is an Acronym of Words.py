
class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        return ''.join([word[0] for word in words]) == s


sol = Solution()
print(sol.isAcronym(["alice", "bob", "charlie"], "abc"))
print(sol.isAcronym(["never", "gonna", "give", "up", "on", "you"], "ngguoy"))