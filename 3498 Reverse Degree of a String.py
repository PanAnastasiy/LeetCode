class Solution:
    def reverseDegree(self, s: str) -> int:
        product = 0
        for i in range(len(s)):
            product += (i + 1) * (123 - ord(s[i]))
        return product


print(Solution().reverseDegree("abc"))
