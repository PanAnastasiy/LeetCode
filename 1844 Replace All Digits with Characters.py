class Solution:
    def replaceDigits(self, s: str) -> str:
        answer = ""
        for index in range(1, len(s), 2):
            answer += s[index - 1] + self.shift(s[index - 1], s[index])
        return answer if len(answer) == len(s) else answer + s[-1]
    def shift(self, letter:str, digit:str) -> str:
        return chr(ord(letter) + int(digit))


sol = Solution()
print(sol.replaceDigits("a1c1e1"))
print(sol.replaceDigits("a1b2c3d4e"))
