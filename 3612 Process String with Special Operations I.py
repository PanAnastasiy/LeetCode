
class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for ch in s:
            if ch.isalpha() and ch.islower():
                result.append(ch)
            elif ch == '*' and result:
                result.pop()
            elif ch == '#':
                result += result
            elif ch == '%':
                result = result[::-1]
        return ''.join(result)


print(Solution().processStr("a#b%*"))
