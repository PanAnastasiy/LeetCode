

class Solution(object):

    @staticmethod
    def countKeyChanges(s: str) -> int:
        total = 0
        s = s.lower()
        for index in range(1, len(s)):
            if s[index] != s[index-1]:
                total += 1
        return total


print(Solution.countKeyChanges("AaAaAaaA"))

