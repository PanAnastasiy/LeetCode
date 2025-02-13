
class Solution:
    def greatestLetter(self, s: str) -> str:
        s = sorted(s, reverse=True)
        if not s[-1].isupper():
            return ''
        for i in range(len(s)):
            if s[i].isupper():
                return ''
            if s[i].upper() in s:
                return s[i].upper()


sol = Solution()
print(sol.greatestLetter("lEeTcOdE"))
print(sol.greatestLetter("arRAzFif"))
print(sol.greatestLetter("AbCdEfGhIjK"))
