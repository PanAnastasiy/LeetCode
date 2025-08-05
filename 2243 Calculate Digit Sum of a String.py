class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            parts = []
            for i in range(0, len(s), k):
                digits = list(map(int, s[i:i+k]))
                parts.append(str(sum(digits)))
            s = ''.join(parts)
        return s


print(Solution().digitSum("00000000", k = 3))
