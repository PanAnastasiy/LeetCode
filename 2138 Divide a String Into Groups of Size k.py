
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        s += (len(s) % k != 0) * (k - len(s) % k) * fill
        return [s[i: i + k] for i in range(0, len(s), k)]


sol = Solution()
print(sol.divideString("12345678", 3, "x"))
print(sol.divideString("abcdefghij", 3, "x"))
print(sol.divideString(s = "abcdefghi", k = 3, fill = "x"))