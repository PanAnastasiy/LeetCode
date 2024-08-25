class Solution:
    def countAsterisks(self, s: str) -> int:
        return ''.join(s.split('|')[::2]).count('*')


sol = Solution()
print(sol.countAsterisks("yo|uar|e**|b|e***au|tifu|l"))
