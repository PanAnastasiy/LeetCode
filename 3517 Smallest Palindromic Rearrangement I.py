class Solution:
    def smallestPalindrome(self, s: str) -> str:
        l = len(s)
        first_part = ''.join(sorted(s[:l // 2]))
        second_part = ''.join(sorted(s[l // 2 + l % 2:]))
        return first_part + s[l // 2: l // 2 + l % 2] + second_part[::-1]


print(Solution().smallestPalindrome("babab"))
print(Solution().smallestPalindrome("daccad"))
