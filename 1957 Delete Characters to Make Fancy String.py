class Solution:
    def makeFancyString(self, s: str) -> str:
        answer = s[0:2]
        for i in range(2, len(s)):
            if s[i] != answer[-1] or answer[-1] != answer[-2]:
                answer += s[i]
        return answer


print(Solution().makeFancyString("leeetcode"))