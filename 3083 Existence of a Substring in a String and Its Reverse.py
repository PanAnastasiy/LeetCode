
class Solution(object):
    @staticmethod
    def isSubstringPresent(s: str) -> bool:
        stack = s[::-1]
        for i in range(1, len(s)):
            if stack[i - 1: i + 1] in s:
                return True
        return False


print(Solution.isSubstringPresent("abcd"))

