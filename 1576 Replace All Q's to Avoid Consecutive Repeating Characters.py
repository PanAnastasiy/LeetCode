class Solution:
    def modifyString(self, s: str) -> str:

        def findLetter(ch1, ch2):
            for letter in 'abc':
                if letter != ch1 and letter != ch2:
                    return letter

        for i in range(len(s)):
            if s[i] == '?':
                s = s.replace(s[i], findLetter(s[i - 1], s[(i + 1) % len(s)]), 1)
        return s


print(Solution().modifyString("a?b?c"))
